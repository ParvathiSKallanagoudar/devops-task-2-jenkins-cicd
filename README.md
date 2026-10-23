# Task 2: Simple Jenkins CI/CD Pipeline

## Project Overview

This project demonstrates a simple Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins and Docker. The pipeline automatically builds a Docker image, runs unit tests, and deploys a Python web application in a Docker container.

## Objectives

- Automate application building using Jenkins.
- Containerize the application using Docker.
- Execute automated unit tests.
- Deploy the application in a Docker container.
- Configure Jenkins to check GitHub for code changes using Poll SCM.

## Technologies Used

- **Jenkins** – CI/CD automation
- **Docker** – Application containerization and deployment
- **Python 3.12** – Application development
- **Git and GitHub** – Version control and source code management
- **Python unittest** – Automated testing

## Project Structure

```text
devops-task-2-jenkins-cicd/
├── app.py
├── test_app.py
├── Dockerfile
├── Jenkinsfile
├── .gitignore
└── README.md
```

## Application Details

The application is a simple Python HTTP server that listens on port 8000 and returns the following response:

`Hello from Elevate Labs Task 2 - Jenkins CI/CD!`

## Jenkins Pipeline Stages

### 1. Build
Jenkins builds a Docker image named `elevate-task-2-app:latest` using the Dockerfile.

### 2. Test
Jenkins runs the Python unit test inside the Docker image to verify that the application returns an HTTP 200 response and the expected message.

### 3. Deploy
After successful testing, Jenkins starts the application in a Docker container named `elevate-task-2-app`, mapping host port 8000 to container port 8000.

## How to Run Locally

### Build the Docker image

```bash
docker build -t elevate-task-2-app:latest .
```

### Run the unit test

```bash
docker run --rm --entrypoint python elevate-task-2-app:latest -m unittest -v test_app.py
```

### Deploy the application

```bash
docker run -d --name elevate-task-2-app -p 8000:8000 elevate-task-2-app:latest
```

Open `http://localhost:8000` in your browser to verify the application response.

To stop and remove the container:

```bash
docker rm -f elevate-task-2-app
```

## Jenkins Configuration

1. Create a Pipeline job in Jenkins.
2. Select **Pipeline script from SCM**.
3. Select Git as the source control system.
4. Configure the GitHub repository URL.
5. Set the branch specifier to `*/main`.
6. Set the script path to `Jenkinsfile`.
7. Enable **Poll SCM** with the schedule `H/5 * * * *` to check for new commits approximately every five minutes.

## Verification Results

The pipeline was executed successfully in Jenkins.

- Docker image build: Successful
- Automated unit test: Passed
- Application deployment: Successful
- Browser verification: Successful

## Learning Outcomes

- Understanding Jenkins declarative pipelines.
- Automating build, test, and deployment stages.
- Building and running Docker containers through Jenkins.
- Integrating Jenkins with a GitHub repository.
- Configuring source control polling for automated builds.

## Repository

GitHub: https://github.com/ParvathiSKallanagoudar/devops-task-2-jenkins-cicd

---

**Task:** Elevate Labs Internship – Task 2  
**Project:** Simple Jenkins CI/CD Pipeline using Docker
