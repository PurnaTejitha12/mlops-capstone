from fastapi import FastAPI
from pydantic import BaseModel

from app.model import predict


app = FastAPI(
    title="W12 MLOps ML API",
    description="Production-style ML API for MLOps training",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    features: list[float]


@app.get("/")
def root():
    return {
        "message": "W12 MLOps ML API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def make_prediction(request: PredictionRequest):
    result = predict(request.features)

    return {
        "prediction": result
    }