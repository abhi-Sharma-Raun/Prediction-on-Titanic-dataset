from fastapi import FastAPI
from fastapi import Response,status,HTTPException
from typing import Optional
from pydantic import BaseModel,Field
from enum import Enum
import pickle
import pandas as pd

pipe=pickle.load(open('model_pipe.pkl','rb'))

app=FastAPI()

class Gender(str,Enum):
    male="male"
    female="female"

class Place_of_Departure(str,Enum):
    S="S"
    C="C"
    Q="Q"

class database_structure(BaseModel):
    Pclass:int=Field(...,ge=1,le=3,description="its' value must be from {1,2,3}")
    Sex:Gender
    Age:float=Field(...,gt=0,description="age must be positive")
    Embarked:Place_of_Departure
    family_size:int=Field(...,ge=1,description="there must be at least 1 family size")
    individual_fare:float=Field(...,gt=0,description="the fare must be positive")
    family_type:Optional[str]=None

@app.post("/predict")
def predict(test_example:database_structure):
    try:
       
       data = pd.DataFrame([test_example.model_dump()])

       x=data['family_size'].iloc[0]

       if x==1:
            data.loc[0,'family_type']= "alone"
       elif x<5:
            data.loc[0,'family_type']= "small"
       else:
            data.loc[0,'family_type']="large"

       if data.isnull().any().any():
            raise HTTPException(status_code=400, detail="Input contains missing values.")

       y_pred=pipe.predict(data)[0]
       return {"prediction": "Survived" if y_pred == 1 else "Did not survive"}
    
    except KeyError as e:
       raise HTTPException(status_code=400,detail=f"Invalid input field:{str(e)}")
    except ValueError as e:
       raise HTTPException(status_code=420,detail=f"invalid value:{str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500,details=f"Internal server error:{str(e)}")