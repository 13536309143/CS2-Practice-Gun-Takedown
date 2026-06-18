import cv2
import numpy as np
import mss
import time
import threading
from pynput.mouse import Controller, Button
from ultralytics import YOLO

class AutoTrigger:
    def __init__(self, model_path=r'runs\detect\runs\train\cs2_player_detector\weights\best.pt'):
        self.model = YOLO(model_path)
        self.mouse = Controller()
        self.sct = mss.mss()
        self.running = False
        self.trigger_enabled = False
        self.conf_threshold = 0.5
        self.target_size = (640, 480)
        self.lock = threading.Lock()
        self.show_window = True
        self.aim_tolerance = 30
        
        primary_monitor = self.sct.monitors[1]
        screen_width = primary_monitor['width']
        screen_height = primary_monitor['height']
        
        self.monitor = {
            "top": (screen_height - self.target_size[1]) // 2,
            "left": (screen_width - self.target_size[0]) // 2,
            "width": self.target_size[0],
            "height": self.target_size[1]
        }
        
        self.screen_center_x = self.target_size[0] // 2
        self.screen_center_y = self.target_size[1] // 2
    
    def is_on_target(self, target):
        dx = abs(target['x'] - self.screen_center_x)
        dy = abs(target['y'] - self.screen_center_y)
        return dx <= self.aim_tolerance and dy <= self.aim_tolerance

    def capture_screen(self):
        sct_img = self.sct.grab(self.monitor)
        frame = np.array(sct_img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        return frame

    def detect_players(self, frame):
        results = self.model(frame, verbose=False)
        detections = []
        
        for result in results:
            for box in result.boxes:
                conf = float(box.conf[0])
                if conf >= self.conf_threshold:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    cx = (x1 + x2) / 2
                    cy = (y1 + y2) / 2
                    detections.append({
                        'x': cx,
                        'y': cy,
                        'conf': conf,
                        'box': [x1, y1, x2, y2]
                    })
        
        return detections

    def find_best_target(self, detections):
        if not detections:
            return None
        
        best_target = None
        highest_conf = 0
        
        for det in detections:
            if det['conf'] > highest_conf:
                highest_conf = det['conf']
                best_target = det
        
        return best_target

    def trigger(self, target):
        with self.lock:
            if not self.trigger_enabled:
                return
            
            self.mouse.click(Button.left, 1)
            print(f"触发! 置信度: {target['conf']:.2f}")

    def draw_detections(self, frame, detections, best_target):
        for det in detections:
            x1, y1, x2, y2 = det['box']
            conf = det['conf']
            is_best = det == best_target
            
            color = (0, 0, 255) if is_best else (0, 255, 0)
            thickness = 2 if is_best else 1
            
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
            
            label = f"Player: {conf:.2f}"
            (label_width, label_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            cv2.rectangle(frame, (int(x1), int(y1) - 20), (int(x1) + label_width, int(y1)), color, -1)
            cv2.putText(frame, label, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        cv2.circle(frame, (self.screen_center_x, self.screen_center_y), 5, (255, 0, 0), -1)
        
        trigger_status = "ON" if self.trigger_enabled else "OFF"
        status_color = (0, 255, 0) if self.trigger_enabled else (0, 0, 255)
        cv2.putText(frame, f"Trigger: {trigger_status}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
        cv2.putText(frame, f"FPS: {self.fps:.1f}", (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        return frame

    def run(self):
        print("自动扳机程序启动!")
        print(f"模型: {self.model.__class__.__name__}")
        print(f"置信度阈值: {self.conf_threshold}")
        print("按 'F1' 切换自动扳机开关")
        print("按 'F2' 切换显示窗口")
        print("按 'ESC' 退出")
        
        self.running = True
        self.fps = 0
        frame_count = 0
        start_time = time.time()
        
        while self.running:
            frame = self.capture_screen()
            detections = self.detect_players(frame)
            best_target = self.find_best_target(detections)
            
            if detections and best_target and self.trigger_enabled and self.is_on_target(best_target):
                self.trigger(best_target)
            
            frame_count += 1
            if frame_count % 30 == 0:
                elapsed_time = time.time() - start_time
                self.fps = frame_count / elapsed_time
            
            if self.show_window:
                frame = self.draw_detections(frame, detections, best_target)
                cv2.imshow('CS2 Auto Trigger - Detection', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == 27:
                    self.stop()
                elif key == ord('f') or key == ord('F'):
                    self.toggle_trigger()
            
            time.sleep(0.001)
        
        cv2.destroyAllWindows()

    def toggle_trigger(self):
        with self.lock:
            self.trigger_enabled = not self.trigger_enabled
            state = "开启" if self.trigger_enabled else "关闭"
            print(f"自动扳机 {state}")

    def toggle_window(self):
        self.show_window = not self.show_window
        state = "显示" if self.show_window else "隐藏"
        print(f"显示窗口 {state}")

    def stop(self):
        self.running = False
        print("程序退出")

def key_listener(auto_trigger):
    from pynput.keyboard import Listener, Key
    
    def on_press(key):
        if key == Key.f1:
            auto_trigger.toggle_trigger()
        elif key == Key.f2:
            auto_trigger.toggle_window()
        elif key == Key.esc:
            auto_trigger.stop()
            return False
    
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    auto_trigger = AutoTrigger()
    
    listener_thread = threading.Thread(target=key_listener, args=(auto_trigger,))
    listener_thread.daemon = True
    listener_thread.start()
    
    try:
        auto_trigger.run()
    except KeyboardInterrupt:
        auto_trigger.stop()
    finally:
        auto_trigger.sct.close()
        cv2.destroyAllWindows()