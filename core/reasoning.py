def analyze_environment(detections, scene, mood):
    objects = [d["object"] for d in detections]

    risk_level = "Normal"
    alert = None

    if mood == "night" and "person" in objects:
        risk_level = "Low Visibility"

    if scene == "mountain" and mood == "cloudy":
        alert = "Possible Fog Conditions"

    if "water" in objects and scene == "beach":
        alert = "Coastal Area"

    return {
        "risk_level": risk_level,
        "alert": alert
    }