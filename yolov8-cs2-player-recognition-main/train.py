from ultralytics import YOLO
import os

def main():
    model = YOLO('yolov8n.pt')
    
    results = model.train(
        data='data.yaml',
        epochs=100,
        batch=16,
        imgsz=640,
        device='0',
        workers=8,
        optimizer='AdamW',
        lr0=0.001,
        weight_decay=0.0005,
        momentum=0.937,
        patience=10,
        verbose=True,
        project='runs/train',
        name='cs2_player_detector',
        exist_ok=True,
        augment=True,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=0.0,
        translate=0.1,
        scale=0.5,
        shear=0.0,
        perspective=0.0,
        flipud=0.0,
        fliplr=0.5,
        mosaic=1.0,
        mixup=0.0,
        copy_paste=0.0,
        val=True
    )
    
    print("\n训练完成！模型保存在 runs/train/cs2_player_detector/")
    print(f"最佳模型: {results.best}")

if __name__ == '__main__':
    os.chdir(r'D:\CS2 Practice Gun Takedown\yolov8-cs2-player-recognition-main')
    main()