from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "iris_model.joblib"


def train_model():
    iris = load_iris()

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(iris.data, iris.target)

    MODEL_DIR.mkdir(exist_ok=True)

    joblib.dump(
        {
            "model": model,
            "target_names": iris.target_names,
        },
        MODEL_PATH,
    )

    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
