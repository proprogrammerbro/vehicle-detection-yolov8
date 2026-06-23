from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r"C:\Users\mrsrt\Downloads\AI_sample\runs\detect\vehicle_detector-3\weights\best.pt")
    model.predict(source=0, show=True, conf=0.5)