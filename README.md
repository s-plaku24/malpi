# Iris Prediction API

A FastAPI service that predicts iris species using machine learning.

## Features
- Machine learning-powered iris species prediction
- Token-based authentication
- Automatic API documentation
- Dockerized deployment

## API Endpoints
- POST /hello - Greeting endpoint
- POST /predict - Iris species prediction (requires API token)

## Deployed API
- API: https://iris.yourdomain.com
- Documentation: https://iris.yourdomain.com/docs

## Usage
Send POST request to /predict with X-API-Token header and JSON body containing sepal_length, sepal_width, petal_length, and petal_width.