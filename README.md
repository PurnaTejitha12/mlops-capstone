Iris Flower Prediction API — MLOps
Overview

This project is a production-oriented machine learning application that predicts the species of an Iris flower based on its sepal and petal measurements.

The ML model is exposed through a FastAPI REST API and packaged using Docker. The project also implements a CI pipeline with GitHub Actions to automatically validate code quality, run tests, and verify the Docker image build.

The goal is to demonstrate how a machine learning model can be developed and maintained as a reliable software application using fundamental MLOps practices.

How It Works

The application receives four flower measurements:

Sepal length
Sepal width
Petal length
Petal width

These values are passed to the prediction model, which returns the predicted Iris species.

Example:

{
  "features": [5.1, 3.5, 1.4, 0.2]
}


The prediction service is available through the /predict API endpoint, while /health is provided to verify that the service is running.

MLOps Implementation

This project focuses on making the ML application reproducible, testable, and deployment-ready.

API

FastAPI is used to expose the machine learning model as a REST service. The API provides input validation and endpoints for prediction and health checks.

Testing

Pytest is used to automatically test the API endpoints.

The current test suite validates:

Root endpoint
Health endpoint
Prediction endpoint
pytest -v


Current result:

3 passed

Code Quality

Ruff is used to check Python code quality and formatting.

ruff check .


This prevents common code-quality issues from entering the CI pipeline.

Docker

The application is containerised using Docker so that the API and its runtime dependencies can be executed consistently across environments.

Build the image:

docker build -t w12-mlops-api .


Run the application:

docker run -p 8000:8000 w12-mlops-api


The API can then be accessed at:

http://localhost:8000


Interactive API documentation is available through FastAPI at:

http://localhost:8000/docs

CI Pipeline

GitHub Actions is used to automatically validate changes pushed to the repository.

The pipeline performs:

Code Checkout
      ↓
Dependency Installation
      ↓
Ruff Linting
      ↓
Pytest
      ↓
Docker Image Build


This ensures that code changes are checked before they are merged into the main branch.

Monitoring Strategy

For a production deployment, the application should be monitored at both the API and model levels.

The main application metrics are:

Request volume
API response latency
Error rate
CPU utilisation
Memory utilisation

The ML-specific metrics include:

Model accuracy
Prediction distribution
Input data drift
Feature drift
Model performance degradation

Alerts should be triggered when API performance or model quality falls below defined thresholds.

Model Retraining

Model retraining should be considered when production data changes significantly or model performance decreases.

Typical retraining triggers include:

Model accuracy falling below the required threshold
Significant input data drift
Changes in feature distributions
Availability of new labelled training data

A future production workflow can automate this process by collecting new data, retraining the model, evaluating the new version, and deploying it only when it meets the required performance criteria.

Git Workflow

Development is performed on the dedicated feature branch:

feat/aiml-W12-purnatejitha


Changes are committed, pushed to GitHub, validated through GitHub Actions, and submitted through a Pull Request before being merged into main.

Technologies

Python · FastAPI · Pytest · Ruff · Docker · Git · GitHub Actions · MLOps

Objective

The objective of this project is to demonstrate the complete foundation of an MLOps workflow by taking a machine learning prediction model and turning it into a tested, containerised, and continuously validated API that can be extended toward full production deployment and monitoring.