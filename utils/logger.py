import pandas as pd
from datetime import datetime

def log_prediction(scene, mood, risk, fps):
    data = {
        "timestamp": datetime.now(),
        "scene": scene,
        "mood": mood,
        "risk_level": risk,
        "fps": fps
    }

    df = pd.DataFrame([data])
    df.to_csv("logs.csv", mode='a', header=False, index=False)