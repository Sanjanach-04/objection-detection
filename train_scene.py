from ultralytics import YOLO

# Load pretrained classification model
model = YOLO("yolov8n-cls.pt")

# Train on your dataset
model.train(
    data="datasets/scene_dataset",
    epochs=20,
    imgsz=224,
    batch=16
)