🌸 Iris Flower Prediction API — MLOps Capstone

A production-oriented Machine Learning application that predicts the species of an Iris flower from its sepal and petal measurements.

The project demonstrates how a machine learning model can be transformed into a tested, validated, containerised, and deployable REST API using modern MLOps practices.

📌 Project Overview

This project serves a Scikit-learn Iris classification model through a FastAPI REST API.

The application accepts four numerical flower measurements:

Sepal length

Sepal width

Petal length

Petal width

The model predicts one of the following Iris species:

setosa

versicolor

virginica

Example Input
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example Response
{
  "prediction": "setosa"
}

🏗️ Architecture
                     ┌──────────────────────┐
                     │      User / Client   │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │    HTML/CSS/JS       │
                     │      Frontend        │
                     └──────────┬───────────┘
                                │
                         HTTP POST /predict
                                │
                                ▼
                     ┌──────────────────────┐
                     │       FastAPI        │
                     │      REST API        │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │   Input Validation   │
                     │       Pydantic       │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │    ML Prediction     │
                     │    Scikit-learn      │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ iris_model.joblib    │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Prediction Response  │
                     └──────────────────────┘

✨ Features

Machine learning model serving

FastAPI REST API

Pydantic input validation

Interactive Swagger API documentation

Automated API testing with Pytest

Python linting with Ruff

Docker containerisation

GitHub Actions CI/CD

Docker image building and publishing

Frontend interface using HTML, CSS and JavaScript

API health monitoring

ML monitoring strategy

Model retraining strategy

MLflow-based experiment and model lifecycle management

Git-based development workflow

Cloud deployment ready with Render

📁 Project Structure
mlops-capstone/
│
├── .github/
│   └── workflows/
│       └── mlops-ci.yml
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── model.py
│
├── docs/
│   └── mlops-monitoring.md
│
├── models/
│   └── iris_model.joblib
│
├── my-frontend/
│   └── index.html
│
├── tests/
│   └── test_api.py
│
├── training/
│   ├── __init__.py
│   └── train.py
│
├── .dockerignore
├── .gitignore
├── .python-version
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md

🚀 Running the Project Locally
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd mlops-capstone

2. Install Dependencies
pip install -r requirements.txt

3. Start the FastAPI Server
uvicorn app.main:app --reload --port 8000


The API will be available at:

http://localhost:8000

📖 API Documentation

FastAPI provides interactive Swagger documentation.

Open:

http://localhost:8000/docs

🔌 API Endpoints
GET /

Returns the application status and API version.

Example Response
{
  "message": "W12 MLOps ML API is running",
  "version": "1.0.0"
}

GET /health

Health check endpoint used to verify API availability.

Example Response
{
  "status": "healthy"
}

POST /predict

Accepts four Iris measurements and returns the predicted species.

Request
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Response
{
  "prediction": "setosa"
}

Input Validation

The API requires exactly four numerical features.

Invalid requests are rejected automatically using Pydantic validation.

🧪 Testing

Pytest is used for automated API testing.

Run:

pytest -v


The test suite validates:

Root endpoint

Health endpoint

Prediction endpoint

Invalid feature count

Excess feature count

Current Test Result
5 passed


This ensures that the main API functionality and input validation work as expected.

🔍 Code Quality

Ruff is used for Python linting and code quality validation.

Run:

ruff check .


The same quality checks are integrated into the CI/CD pipeline.

🐳 Docker

The application is containerised using Docker to provide a consistent runtime environment.

Build the Docker Image
docker build -t w12-mlops-api:latest .

Run the Container
docker run -p 8000:8000 w12-mlops-api:latest


The API will be available at:

http://localhost:8000


Swagger documentation:

http://localhost:8000/docs


Health check:

http://localhost:8000/health


Prediction endpoint:

http://localhost:8000/predict

🌐 Frontend

A lightweight frontend is included in:

my-frontend/index.html


The frontend is built using:

HTML

CSS

JavaScript

It provides a simple interface where users can enter:

Sepal length

Sepal width

Petal length

Petal width

The JavaScript sends the measurements to the FastAPI /predict endpoint and displays the predicted Iris species.

Local Frontend

The frontend can be opened directly:

my-frontend/index.html


When running locally, the frontend communicates with:

http://localhost:8000/predict


For production deployment, the API URL should be changed to the deployed Render backend URL.

☁️ Render Deployment

The FastAPI application can be deployed as a Render Web Service.

Backend Configuration

Recommended Render settings:

Service Type:       Web Service
Language:           Python
Branch:             main
Root Directory:     .
Build Command:      pip install -r requirements.txt
Start Command:      uvicorn app.main:app --host 0.0.0.0 --port $PORT


After deployment, Render provides a public API URL such as:

https://your-api-name.onrender.com


The deployed API can then be accessed through:

https://your-api-name.onrender.com/


Health endpoint:

https://your-api-name.onrender.com/health


Swagger documentation:

https://your-api-name.onrender.com/docs


Prediction endpoint:

https://your-api-name.onrender.com/predict


Replace your-api-name with the actual Render service URL.

🌍 Frontend Deployment

The frontend can also be deployed as a Render Static Site.

Recommended configuration:

Service Type:       Static Site
Root Directory:     my-frontend
Publish Directory:  .


The frontend JavaScript should use the deployed FastAPI URL instead of:

http://localhost:8000


For example:

const API_URL = "https://your-api-name.onrender.com";


The prediction request is then sent to:

${API_URL}/predict

🔄 CI/CD Pipeline

GitHub Actions automates the project's continuous integration workflow.

The workflow is located at:

.github/workflows/mlops-ci.yml

Pipeline
        Code Push
            │
            ▼
       GitHub Actions
            │
            ▼
          Ruff
       Code Quality
            │
            ▼
         Pytest
       Automated Tests
            │
            ▼
      Docker Build
       Image Build
            │
            ▼
      Docker Publish
       Docker Hub


The pipeline validates the application before a Docker image is published.

🐳 Docker Image Publishing

The CI/CD workflow is configured to build and publish the Docker image after successful validation.

The image can be published to Docker Hub using the configured GitHub Actions workflow.

This provides a reproducible container image that can be used across different environments.

📊 Monitoring Strategy

Monitoring is considered at both the API level and the machine learning level.

API Metrics

Important operational metrics include:

Request volume

API response latency

P95 latency

Error rate

HTTP status codes

API availability

CPU utilisation

Memory utilisation

ML Metrics

Machine learning monitoring should include:

Model accuracy

Prediction distribution

Model confidence

Input feature distribution

Data drift

Feature drift

Model performance degradation

Detailed monitoring documentation is available in:

docs/mlops-monitoring.md

🚨 Alerting Strategy

Alerts should be configured for important application and model conditions.

Example thresholds include:

Metric	Example Alert Threshold
Error rate	> 5%
P95 latency	> 1 second
CPU utilisation	> 80%
Memory utilisation	> 80%
Data drift	Significant drift detected
Model accuracy	Below production threshold
CI/CD	Pipeline failure
Docker	Build failure

These thresholds are examples and should be adjusted according to the requirements of the production environment.

🔁 Model Retraining Strategy

Model retraining should be considered when production data or model performance changes significantly.

Potential retraining triggers include:

Model accuracy falling below the production threshold

Significant input data drift

Changes in feature distributions

Availability of new labelled training data

Production model performance degradation

A future automated retraining workflow can follow:

Production Data
       │
       ▼
Data Validation
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Performance Check
       │
       ├── Fail ──► Keep Existing Model
       │
       ▼
   Pass
       │
       ▼
Model Versioning
       │
       ▼
Model Deployment


This approach helps prevent an underperforming model from automatically replacing a production model.

🧪 MLflow

MLflow is included as part of the planned MLOps stack for experiment tracking and model lifecycle management.

MLflow can be used to track:

Experiments

Parameters

Metrics

Model artifacts

Model versions

Model versioning improves reproducibility and makes it possible to maintain previous model versions for rollback when required.

🌱 Git Workflow

Development is performed using a dedicated feature branch:

feat/aiml-W12-PurnaTejitha


Recommended workflow:

Feature Branch
      │
      ▼
Code Changes
      │
      ▼
Git Commit
      │
      ▼
Push to GitHub
      │
      ▼
GitHub Actions
      │
      ▼
Pull Request
      │
      ▼
Review / Validation
      │
      ▼
main


Example Git commands:

git checkout -b feat/aiml-W12-PurnaTejitha

git add .

git commit -m "Update Iris prediction application"

git push origin feat/aiml-W12-PurnaTejitha


After validation, the changes can be submitted through a Pull Request and merged into main.

🛠️ Technologies
Technology	Purpose
Python	Application and ML development
Scikit-learn	Machine learning model
FastAPI	REST API
Pydantic	Request validation
Pytest	Automated testing
Ruff	Code quality and linting
Docker	Containerisation
Git	Version control
GitHub	Source code management
GitHub Actions	CI/CD automation
Docker Hub	Container image publishing
MLflow	Experiment and model lifecycle management
Render	Cloud deployment
HTML/CSS/JavaScript	Frontend
🎯 Project Objectives

The main objective of this capstone is to demonstrate the foundation of an end-to-end MLOps workflow by taking a machine learning model and turning it into a reliable, tested, containerised, and deployable application.

The project demonstrates:

Machine learning model serving

REST API development

Input validation

Automated testing

Code quality validation

Docker containerisation

CI/CD automation

Container image publishing

Frontend integration

Cloud deployment

API monitoring strategy

ML monitoring strategy

Model retraining strategy

MLflow-based model lifecycle management

Git-based development workflow

✅ Project Status
Component	Status
ML Model	✅ Complete
FastAPI API	✅ Complete
Input Validation	✅ Complete
API Tests	✅ Complete
Ruff Linting	✅ Configured
Docker	✅ Tested Locally
Frontend	✅ Complete
CORS	✅ Configured
GitHub Actions	✅ Configured
Docker Image Publishing	✅ Configured
Monitoring Documentation	✅ Complete
MLflow Strategy	✅ Documented
Retraining Strategy	✅ Documented
Render Deployment	🚀 Ready
👩‍💻 Author

Purna Tejitha Sanisetty
