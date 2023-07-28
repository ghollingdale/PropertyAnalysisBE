from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import pickle
import json

class propmodel(BaseModel):
    number_of_bedrooms: float
    living_area: float
    fully_equipped_kitchen: float
    furnished: float
    terrace: float
    garden: float
    total_property_area: float
    total_land_area: float
    swimming_pool: float
    state_of_the_building: float


app = FastAPI()
pickle_in = open('data/model.pkl', 'rb')
regressor = pickle.load(pickle_in)

# http://127.0.0.1:8000
@app.get('/')
def home():
    return {"Intro" : "Welcome to the local version of the PropertyAnalysisBE model. Please navigate to 'http://127.0.0.1:8000/docs' and input your data into the '/pricepredict' dropdown to continue. Check that you have read the README.md to format your input correctly."}

# http://127.0.0.1:8000/pricepredict
@app.post('/pricepredict')
def predict(data: propmodel):
    data = data.model_dump_json()
    data = json.loads(data)
    print(data)    
    
    number_of_bedrooms = data['number_of_bedrooms']
    living_area = data['living_area']
    fully_equipped_kitchen = data['fully_equipped_kitchen']
    furnished = data['furnished']
    terrace = data['terrace']
    garden = data['garden']
    total_property_area = data['total_property_area']
    total_land_area = data['total_land_area']
    swimming_pool = data['swimming_pool']
    state_of_the_building = data['state_of_the_building']
    
    prediction = regressor.predict([[
        number_of_bedrooms,
        living_area,
        fully_equipped_kitchen,
        furnished,
        terrace,
        garden,
        total_property_area,
        total_land_area,
        swimming_pool,
        state_of_the_building
    ]])
    return {
        'prediction': round(prediction[0],2)
        }