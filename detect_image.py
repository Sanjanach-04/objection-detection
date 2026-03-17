from ultralytics import YOLO
import cv2
import os

model = YOLO("models/yolov8n.pt")

def detect_image(image_path):
    img = cv2.imread(image_path)
    results = model(img)
    
    annotated = results[0].plot()
    
    output_path = "static/output_images/output.jpg"
    cv2.imwrite(output_path, annotated)
    
    print("Detection complete! Saved to:", output_path)

if __name__ == "__main__":
    detect_image("test.jpg")