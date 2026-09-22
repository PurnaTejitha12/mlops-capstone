from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "iris_model.joblib"

model_data = joblib.load(MODEL_PATH)

model = model_data["model"]
target_names = model_data["target_names"]


def predict(features: list[float]) -> str:
    prediction = model.predict([features])[0]

    return str(target_names[prediction])
