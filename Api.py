from fastapi import FastAPI, HTTPException, Query
import requests
import pickle
from pydantic import BaseModel
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Création de l'application FastAPI
app = FastAPI()

# Chargement du modèle
with open('regression_model.pkl', 'rb') as model_file:
    regression_model = pickle.load(model_file)

# Route pour récupérer les coordonnées et la prédiction en utilisant GET
@app.get("/get_coordinates_and_prediction/")
def get_coordinates_and_prediction(address: str = Query(..., description="Entrez une adresse")):
    # Récupérer les coordonnées
    url = f"https://api-adresse.data.gouv.fr/search/?q={address}"
    print(url)
    breakpoint()
    response = requests.get(url)
    data = response.json()
    if data['features']:
        first_result = data['features'][0]
        coordinates = first_result['geometry']['coordinates']
        longitude, latitude = coordinates

        # Obtenir la prédiction
        prediction = regression_model.predict([[latitude, longitude]])[0]
        prediction_output = round(prediction, 2)

        return {"latitude": latitude, "longitude": longitude, "prediction": prediction_output}
    else:
        raise HTTPException(status_code=404, detail="Aucune coordonnée trouvée pour cette adresse.")

# Modèle de requête POST
class AddressRequest(BaseModel):
    address: str

# Route pour recevoir une demande POST de Dash
@app.post("/get_coordinates_and_prediction/post/")
def get_coordinates_and_prediction_post(request: AddressRequest):
    # Récupérer les coordonnées
    url = f"https://api-adresse.data.gouv.fr/search/?q={request.address}"
    response = requests.get(url)
    data = response.json()
    if data['features']:
        first_result = data['features'][0]
        coordinates = first_result['geometry']['coordinates']
        longitude, latitude = coordinates

        # Obtenir la prédiction
        prediction = regression_model.predict([[latitude, longitude]])[0]
        prediction_output = round(prediction, 2)

        return {"latitude": latitude, "longitude": longitude, "prediction": prediction_output}
    else:
        raise HTTPException(status_code=404, detail="Aucune coordonnée trouvée pour cette adresse.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8012)
