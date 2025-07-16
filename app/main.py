from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Load the ML model (use just 'iris.mdl' for Docker)
model = joblib.load('iris.mdl')

app = FastAPI(
    title="Iris Prediction API",
    description="A FastAPI service that predicts iris species using machine learning.",
    version="1.0.0"
)

class NameRequest(BaseModel):
    name: str

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/hello", summary="Greet the user", response_description="A greeting message")
def hello(data: NameRequest):
    return {"message": f"Hello {data.name}"}

@app.post("/predict", summary="Predict iris species", response_description="Predicted species")
async def predict(features: IrisFeatures, x_api_token: str = Header(...)):
    if x_api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Convert to DataFrame
    df = pd.DataFrame([features.dict()])
    
    # Make prediction
    prediction = model.predict(df)[0]
    
    return {"prediction": prediction}