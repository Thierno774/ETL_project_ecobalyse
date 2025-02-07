from pydantic import BaseModel



class User:
    predictions: float 


test = {
  "predictions_impacts": 4099.261
}


mydata = [User(**data) for data in test]

print(mydata)