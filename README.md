# Iris Species Classifier API

A machine learning API built with FastAPI that predicts iris flower species based on petal and sepal measurements.

## What it does
- Predicts iris species (setosa, versicolor, virginica) from flower measurements
- Uses Random Forest classifier trained on the classic iris dataset
- Secure API with token authentication

## How to use
1. Start the server: `uvicorn app.main:app --reload`
2. Send POST request to `/predict` with your API token
3. Include flower measurements in JSON format

## Example request
```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}