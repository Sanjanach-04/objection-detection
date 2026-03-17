import cv2
import time
from ultralytics import YOLO

detector = YOLO("yolov8s.pt")
scene_model = YOLO("models/scene_cls.pt")

prev_time = time.time()

cap = cv2.VideoCapture(0)

print("Webcam started. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    det_results = detector(frame, verbose=False)
    annotated_frame = det_results[0].plot()

    scene_results = scene_model(frame, verbose=False)
    top1 = scene_results[0].probs.top1
    scene = scene_model.names[top1]

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(annotated_frame, f"Scene: {scene}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(annotated_frame, f"FPS: {round(fps,2)}", (20,70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.imshow("Environmental Scene AI", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()