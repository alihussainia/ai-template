import pandas as pd
from fastapi import FastAPI
import uvicorn
import joblib

# Create the app
app = FastAPI()

# Load trained Pipeline
# Load the saved model from file
model = joblib.load("models/model.pkl")

# Define predict function
@app.post('/predict')
def predict(Age, Experience, Income, Family, CCAvg, Education, Mortgage, SecuritiesAccount, CDAccount, Online, CreditCard):
    
    features=[{
        'Age': Age, 
        'Experience': Experience,
        'Income': Income,
        'Family': Family,
        'CCAvg': CCAvg,
        'Education': Education,	
        'Mortgage': Mortgage,
        'SecuritiesAccount': SecuritiesAccount,	
        'CDAccount': CDAccount,	
        'Online': Online,
        'CreditCard': CreditCard}]
    
    features=pd.DataFrame.from_dict(features)
    predictions = model.predict(features)
    return {'prediction': predictions[0].item()}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)