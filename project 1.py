from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")

    model.train(
        data="C:/Users/mrsrt/Downloads/Vehicle Identification.v1i.yolov8/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        name="vehicle_detector"
    )