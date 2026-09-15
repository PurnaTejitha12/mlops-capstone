Iris Flower Prediction API — MLOps Overview



This project is a production-oriented machine learning application that predicts the species of an Iris flower based on its sepal and petal measurements.



The ML model is exposed through a FastAPI REST API and packaged using Docker. GitHub Actions is used to automate linting, testing, Docker image building, and container image publishing.



How It Works



The application receives four flower measurements:



Sepal length



Sepal width



Petal length



Petal width



Example request:



{

&#x20; "features": \[5.1, 3.5, 1.4, 0.2]

}





The prediction service is available through:



POST /predict





The health check is available through:



GET /health



API



FastAPI provides the REST API with input validation and health monitoring.



Available endpoints:



GET  /

GET  /health

POST /predict





Interactive Swagger documentation:



http://localhost:8000/docs



Testing



Pytest is used to test the API endpoints.



Run:



pytest -v





The current test suite validates:



Root endpoint



Health endpoint



Prediction endpoint



Expected result:



3 passed



Code Quality



Ruff is used for Python linting.



Run:



ruff check .



Docker



The application is containerised using Docker so that the API and its dependencies can run consistently across environments.



Build the Image

docker build -t w12-mlops-api:latest .



Run the Container

docker run -p 8000:8000 w12-mlops-api:latest





The API is then available at:



http://localhost:8000





Swagger documentation:



http://localhost:8000/docs





Health check:



http://localhost:8000/health





The Docker image was successfully built and the container was successfully tested locally.



CI/CD Pipeline



GitHub Actions automates the ML application CI/CD workflow:



Lint

&#x20; ↓

Test

&#x20; ↓

Build Docker Image

&#x20; ↓

Push Docker Image





The workflow is located at:



.github/workflows/mlops-ci.yml





The pipeline uses Ruff for code quality checks, Pytest for automated tests, and Docker for container image builds.



Docker images are configured to be pushed to Docker Hub after successful builds on the main branch.



Monitoring Strategy



The application should be monitored at both API and ML model levels.



API Metrics



The main application metrics are:



Request volume



API response latency



Error rate



HTTP status codes



API availability



CPU utilisation



Memory utilisation



ML Metrics



The ML-specific metrics include:



Model accuracy



Prediction distribution



Model confidence



Input feature distribution



Data drift



Feature drift



Model performance degradation



Alerts



Alerts should be triggered when:



Error rate exceeds 5%



P95 latency exceeds 1 second



CPU utilisation exceeds 80%



Memory utilisation exceeds 80%



Significant data drift is detected



Model accuracy falls below the required threshold



CI/CD pipeline fails



Docker build fails



Detailed monitoring documentation is available in:



docs/mlops-monitoring.md



Model Retraining



Model retraining should be considered when production data changes significantly or model performance decreases.



Typical retraining triggers include:



Model accuracy falling below the production threshold



Significant input data drift



Changes in feature distributions



Availability of new labelled training data



Production model performance degradation



A future production workflow can collect new data, retrain the model, evaluate the new model version, and deploy it only when it meets the required performance criteria.



MLflow



MLflow is included as part of the MLOps stack for experiment and model lifecycle management.



MLflow can track:



Experiments



Parameters



Metrics



Model artifacts



Model versions



Model versioning supports reproducibility and allows previous model versions to be restored when required.



Git Workflow



Development is performed on the dedicated feature branch:



feat/aiml-W12-PurnaTejitha





Changes are committed with descriptive messages, pushed to GitHub, validated through GitHub Actions, and submitted through a Pull Request before being merged into main.



Technologies



Python · FastAPI · Scikit-learn · Pytest · Ruff · Docker · Git · GitHub Actions · MLflow · MLOps



Objective



The objective of this project is to demonstrate the foundation of an MLOps workflow by taking a machine learning prediction model and turning it into a tested, containerised, continuously validated API.



The project demonstrates:



Machine learning model serving



REST API development



Automated testing



Code quality validation



Docker containerisation



CI/CD automation



Container image publishing



MLOps monitoring



Model retraining strategies



MLflow-based model lifecycle management

