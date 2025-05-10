from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    ph: float
    soil_humidity: float
    temperature: float
    humidity: float
    rainfall: float

@app.post("/crop-suitability/")
def crop_suitability(data: CropInput):
    return {
        "Crop Suitability": "Rice",
        "Rainfall (mm)": data.rainfall,
        "Recommendations": ["Ensure irrigation", "Maintain pH level"]
    }
