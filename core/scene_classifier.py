from ultralytics import YOLO

class SceneClassifier:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def classify(self, frame):
        results = self.model(frame, verbose=False)
        top1 = results[0].probs.top1
        conf = float(results[0].probs.top1conf)

        return {
            "scene": self.model.names[top1],
            "confidence": round(conf, 2)
        }