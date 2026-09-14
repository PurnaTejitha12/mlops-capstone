from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def train_model():
    iris = load_iris()

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(iris.data, iris.target)

    return model, iris.target_names


model, target_names = train_model()


def predict(features: list[float]) -> str:
    prediction = model.predict([features])[0]

    return str(target_names[prediction])