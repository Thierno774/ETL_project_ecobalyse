from fastapi import FastAPI, Body, Depends, HTTPException, status, Security
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import joblib 
import numpy as np 
from typing import Optional
#from typing import Annotated
from fastapi.security import api_key
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Create an API KEY 
api_key_header = api_key.APIKeyHeader(name = "X-API-KEY")
async def validate_api_key(key : str = Security (api_key_header)): 
    if key != settings.API_KEY: 
        raise HTTPException (
                status_code = 401, 
                detail = "Unauthorized - API Key is wrong"
        )
    return None



## Load Linear Regressor 
filename = '/code/app/models/model.jolib'

model = joblib.load(filename)
print(model.feature_names_in_)


app = FastAPI(openapi_tags = [{
                    "name": "API for Prediction of Impact",
                    "description": "default functions"
}], 
                title = "Ecobalyse Project", 
                description = "My owner API",
                contact = {
                        "name" : "Thierno BAH", 
                        "email" : "thiernosidybah232@gmail.com"
                        })


## Include authentification
#app.include_router(auth.router)

# Create a base Model 

class Ecobalyse(BaseModel): 
    mass : Optional[float] = 0.94
    product	: Optional[int] = 0 
    making_waste: Optional[int] = 1
    yarn_size: Optional[float] = 2.5
    physical_durability : Optional[float] = 3.5
    making_dead_stock: Optional[float] = 1.5
    fabric_process : Optional[float] = 2.5
    price : Optional[float]  = 1.5
    air_transport_ratio: Optional[float] = 1.5
    country_dyeing : Optional[int] = 1
    country_fabric : Optional[int] =1





@app.get("/")
async def root():
    """
    Check if API is working 
    Return a message if the API is working
    """
    return {"message": "API is working"}


# create a post for predict data 
@app.post("/predict")
async def predict_impact(data: Ecobalyse):
    new_data = [[ 
                data.mass,
                data.product ,
                data.making_waste,
                data.yarn_size ,
                data.physical_durability,
                data.making_dead_stock,
                data.fabric_process,
                data.price,
                data.air_transport_ratio ,
                data.country_dyeing	,
                data.country_fabric 
               
     ]]
    # Make Prediction 
    predictions = round(model.predict(new_data)[0],3)
   
    return {"predictions_impacts" : predictions}
