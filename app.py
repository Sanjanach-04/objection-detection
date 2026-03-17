import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

st.title("Environmental Scene Detection AI")

detector = YOLO("yolov8s.pt")
scene_model = YOLO("models/scene_cls.pt")

uploaded_file = st.file_uploader("Upload an image")

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    det_results = detector(frame)
    annotated_frame = det_results[0].plot()

    scene_results = scene_model(frame)
    top1 = scene_results[0].probs.top1
    scene = scene_model.names[top1]

    st.image(annotated_frame, channels="BGR")

    st.write(f"Predicted Scene: {scene}")