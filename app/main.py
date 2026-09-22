from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.model import predict

app = FastAPI(
    title="W12 MLOps ML API",
    description="Production-style ML API for Iris flower prediction",
    version="1.0.0",
)

# Allow the frontend HTML page to call the FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictionRequest(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=4,
        max_length=4,
        description="Iris measurements: sepal length, sepal width, "
        "petal length, petal width",
    )


@app.get("/")
def root():
    return {
        "message": "W12 MLOps ML API is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/predict")
def make_prediction(request: PredictionRequest):
    result = predict(request.features)

    return {
        "prediction": result,
    }
