# /!\ This is a school project

# Health Calculator Service

A FastAPI-based web service that calculates health metrics like BMI (Body Mass Index) and BMR (Basal Metabolic Rate).

## Features

- Calculate BMI based on height and weight
- Calculate BMR based on height, weight, age, and gender
- RESTful API endpoints
- Web interface for easy interaction
- Containerized deployment support
- CI/CD pipeline with GitHub Actions

## Project Structure

```plaintext
.
├── .github/workflows/ci-cd.yml
├── Dockerfile
├── Makefile
├── app.py
├── health_utils.py
├── readme.md
├── requirements.txt
├── templates
│   └── index.html
└── test.py
```

## Local Development

### Prerequisites

- Python 3.12
- Make utility
- pip (Python package installer)

### Setup and Running

1. Clone the repository and navigate into the project directory
2. Create a virtual environment

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment

   ```bash
   source venv/bin/activate
   ```

4. Install dependencies

   ```bash
   make init
   ```

5. Start the development server

   ```bash
   make run
   ```

The frondend will be available at `http://localhost:5001` and the API at `http://localhost:5001/docs`

### Running Tests

Execute the test suite using `make test`

## Deployment

### Building Docker Image Locally

Build the container image using `make build`

### Azure Web App Deployment

This project is configured for automatic deployment to Azure Web App using GitHub Actions.

#### Prerequisites for Azure Deployment

1. Create an Azure Web App:
   - Go to Azure Portal
   - Create a new Web App resource
   - Select Docker Container as the publish method
   - Choose Linux as the operating system
   - Select appropriate region and plan

2. Configure GitHub Secrets:
   - In your GitHub repository, go to Settings > Secrets and variables > Actions
   - Add a new secret named `AZURE_WEBAPP_PUBLISH_PROFILE`
   - Copy the publish profile from your Azure Web App (Download from Overview)
   - Paste the content into the secret value

#### Deployment Process

1. The CI/CD pipeline is triggered automatically on pushes to the main branch
2. The workflow:
   - Runs tests
   - Builds the Docker image
   - Pushes to GitHub Container Registry
   - Deploys to Azure Web App

The deployment can be monitored in the Actions tab of your GitHub repository.

## API Endpoints

### POST /bmi

Calculate Body Mass Index

**Parameters:**

- `height` (float): Height in centimeters
- `weight` (float): Weight in kilograms

### POST /bmr

Calculate Basal Metabolic Rate

**Parameters:**

- `height` (float): Height in centimeters
- `weight` (float): Weight in kilograms
- `age` (int): Age in years
- `gender` (string): Either "male" or "female"
