from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        detections = []

        for box in det_results[0].boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = f"{detector.names[cls_id]} {conf:.2f}"

            detections.append({
                "object": label,
                "confidence": round(conf, 2)
            })

        return detections, results[0].plot()