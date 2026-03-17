from flask import Flask, request, jsonify
import cv2
import numpy as np

from core.detection import ObjectDetector
from core.scene_classifier import SceneClassifier
from core.mood_classifier import MoodClassifier
from core.reasoning import analyze_environment

app = Flask(__name__)

detector = ObjectDetector("../models/yolo_detection.pt")
scene_model = SceneClassifier("../models/scene_cls.pt")
mood_model = MoodClassifier("../models/mood_cls.pt")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img = cv2.imdecode(
        np.frombuffer(file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )

    detections, _ = detector.detect(img)
    scene_result = scene_model.classify(img)
    mood_result = mood_model.classify(img)

    reasoning = analyze_environment(
        detections,
        scene_result["scene"],
        mood_result["mood"]
    )

    return jsonify({
        "scene": scene_result,
        "mood": mood_result,
        "detections": detections,
        "reasoning": reasoning
    })

if __name__ == "__main__":
    app.run(debug=True)