🌸 Iris Flower Prediction — MLOps Capstone

A production-style Machine Learning API for Iris flower classification, built with FastAPI, scikit-learn, Docker, automated testing, and a web-based frontend.

📌 Project Overview

This project demonstrates an end-to-end MLOps workflow for serving a trained Machine Learning model through a REST API.

The application takes four Iris flower measurements as input and predicts the species:

🌱 Setosa

🌿 Versicolor

🌺 Virginica

The trained model is loaded using joblib and served through a FastAPI application. A simple HTML/CSS/JavaScript frontend communicates with the API and displays the prediction.

🏗️ Architecture
                    ┌─────────────────────┐
                    │    Web Browser      │
                    │ HTML / CSS / JS     │
                    └──────────┬──────────┘
                               │
                               │ HTTP POST
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │      /predict       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   ML Model          │
                    │ iris_model.joblib   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Iris Prediction     │
                    │ setosa / versicolor │
                    │ / virginica         │
                    └─────────────────────┘

Deployment Architecture
             GitHub Repository
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   Render Web Service   Render Static Site
        FastAPI              Frontend
          │                   │
          │◄──── HTTPS ──────┘
          │
          ▼
   iris_model.joblib

✨ Features

🚀 FastAPI REST API

🤖 Machine Learning prediction using scikit-learn

🌸 Iris flower classification

✅ Pydantic request validation

🩺 Health-check endpoint

🧪 Automated API tests with pytest

🐳 Docker containerization

🌐 HTML/CSS/JavaScript frontend

🔒 CORS support for frontend-to-API communication

📦 Serialized ML model using Joblib

🔄 GitHub-based deployment workflow

☁️ Ready for Render deployment

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
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md

🧠 Machine Learning Model

The application uses the classic Iris dataset.

The model receives four numerical features:

Feature	Description	Unit
Sepal Length	Length of the sepal	cm
Sepal Width	Width of the sepal	cm
Petal Length	Length of the petal	cm
Petal Width	Width of the petal	cm

The model predicts one of:

setosa
versicolor
virginica


The trained model is stored at:

models/iris_model.joblib

🚀 API
Base URL
Local
http://localhost:8000

Production

After deploying to Render:

https://YOUR-RENDER-API.onrender.com

GET /

Returns basic API information.

Example
curl http://localhost:8000/

Response
{
  "message": "W12 MLOps ML API is running",
  "version": "1.0.0"
}

GET /health

Health-check endpoint used to verify that the API is running.

Example
curl http://localhost:8000/health

Response
{
  "status": "healthy"
}

POST /predict

Predicts the Iris flower species.

Request
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example
curl -X POST "http://localhost:8000/predict" ^
-H "Content-Type: application/json" ^
-d "{\"features\":[5.1,3.5,1.4,0.2]}"

Response
{
  "prediction": "setosa"
}

📖 Interactive API Documentation

FastAPI automatically provides interactive Swagger documentation.

After starting the application, open:

http://localhost:8000/docs


You can test /health and /predict directly from the browser.

Alternative OpenAPI documentation:

http://localhost:8000/redoc

💻 Run Locally
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL


Navigate into the project:

cd mlops-capstone

2. Create a virtual environment
Windows
python -m venv .venv


Activate it:

.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run tests
pytest -v


Expected result:

5 passed

5. Start the API
uvicorn app.main:app --reload --port 8000


The API will be available at:

http://localhost:8000


Swagger documentation:

http://localhost:8000/docs

🌐 Run the Frontend

The frontend is located in:

my-frontend/index.html


Start the API first:

uvicorn app.main:app --reload --port 8000


Then open:

my-frontend/index.html


in your browser.

The frontend sends prediction requests to:

http://localhost:8000/predict


For production deployment, replace the localhost API URL with the Render API URL.

🐳 Docker

The project includes a Dockerfile for containerized deployment.

Build the Docker image
docker build -t w12-mlops-api:latest .

Run the container
docker run -d --name mlops-api -p 8000:8000 w12-mlops-api:latest

Check running containers
docker ps

Test the container
curl http://localhost:8000/health


Expected:

{
  "status": "healthy"
}

🧪 Testing

The project uses pytest for automated API testing.

Current test coverage includes:

Root endpoint

Health endpoint

Valid prediction request

Invalid number of features

Too many features

Run:

pytest -v


Example:

tests/test_api.py::test_root PASSED
tests/test_api.py::test_health PASSED
tests/test_api.py::test_prediction PASSED
tests/test_api.py::test_prediction_rejects_wrong_number_of_features PASSED
tests/test_api.py::test_prediction_rejects_too_many_features PASSED

5 passed

🔄 CI/CD

The project contains a GitHub Actions workflow:

.github/workflows/mlops-ci.yml


The workflow can be used to automatically run project checks whenever changes are pushed to GitHub.

Typical workflow:

Developer
    │
    ▼
Git Commit
    │
    ▼
Git Push
    │
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Install dependencies
    ├── Run tests
    └── Validate project

☁️ Render Deployment

The FastAPI application can be deployed to Render as a Web Service.

Backend Configuration

Create a new Web Service in Render and connect your GitHub repository.

Use:

Setting	Value
Runtime	Python
Branch	main
Root Directory	Leave blank
Build Command	pip install -r requirements.txt
Start Command	uvicorn app.main:app --host 0.0.0.0 --port $PORT

After deployment, Render provides a public API URL.

Example:

https://your-api-name.onrender.com


Test:

https://your-api-name.onrender.com/health


Swagger:

https://your-api-name.onrender.com/docs

Frontend Deployment

The frontend can be deployed separately as a Render Static Site.

Frontend directory:

my-frontend


The frontend must use the deployed API URL instead of:

http://localhost:8000


For example:

const API_URL = "https://your-api-name.onrender.com";


The prediction request becomes:

fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        features: features
    })
});

🔧 Git Workflow

After making changes:

git status


Add files:

git add .


Commit:

git commit -m "Update ML API and frontend"


Push:

git push origin main

📊 Example Prediction
Input
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Output
{
  "prediction": "setosa"
}

🛠️ Technology Stack
Technology	Purpose
Python	Application & ML development
FastAPI	REST API
Pydantic	Request validation
scikit-learn	Machine Learning
Joblib	Model serialization
Pytest	Automated testing
Docker	Containerization
HTML	Frontend structure
CSS	Frontend styling
JavaScript	API communication
GitHub	Version control & CI
Render	Cloud deployment
🎯 MLOps Workflow
        ┌──────────────────┐
        │ Model Training   │
        │ training/train.py│
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Trained Model    │
        │ .joblib          │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ FastAPI Service  │
        │ /predict         │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Automated Tests  │
        │ pytest           │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ GitHub Actions   │
        │ CI               │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Docker / Render  │
        │ Deployment       │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Production API   │
        └──────────────────┘

📌 Project Status
Component	Status
ML Model	✅ Complete
FastAPI API	✅ Complete
Input Validation	✅ Complete
Health Check	✅ Complete
Automated Tests	✅ Complete
Docker	✅ Complete
Frontend	✅ Complete
GitHub	✅ Ready
Render Backend	🚀 Ready for deployment
Render Frontend	🚀 Ready for deployment
👩‍💻 Author

PurnaTejitha

MLOps Capstone Project

⭐ Project Summary

This project demonstrates how a Machine Learning model can be transformed into a production-style application using:

Machine Learning → API → Testing → Docker → CI/CD → Cloud Deployment → Web Frontend

The final application provides an accessible web interface for making Iris flower predictions through a deployed Machine Learning API.