# Vehicle Detection using YOLOv8

Real-time vehicle detection system built with YOLOv8, trained on a custom dataset of 2,188 images.

## Demo
Point a webcam at any traffic footage and the model detects vehicles in real time.

## Classes Detected
Car, Truck, Bus, Motorcycle, Bicycle, Van, Pickup, Jeep, Tricycle, and more (13 classes total)

## Model Performance
- mAP50: 84.1%
- Precision: 82.8%
- Recall: 78.9%

## Tech Stack
- Python
- YOLOv8 (Ultralytics)
- PyTorch (CUDA - trained on NVIDIA RTX 5060)
- OpenCV

## How to Run
### Install dependencies
pip install ultralytics torch torchvision

### Run live detection
python detect_vehicle.py

### Train custom model
python "project 1.py"

## Dataset
Vehicle Identification dataset from Roboflow Universe — 2,188 images, 13 vehicle classes.

## Results
Trained for 50 epochs on NVIDIA RTX 5060 GPU.
