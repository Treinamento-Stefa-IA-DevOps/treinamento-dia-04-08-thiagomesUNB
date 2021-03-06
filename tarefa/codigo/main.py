import pickle
from fastapi import FastAPI,Response, status
import os

app = FastAPI()

@app.post('/model',status_code=200)
## Coloque seu codigo na função abaixo
async def titanic(Sex:int,Age:float,Lifeboat: int,Pclass:int,response: Response):
    with open('model/Titanic.pkl', 'rb') as fid: 
    
        titanic = pickle.load(fid)

        y_pred = bool(titanic.predict([[Sex,Age,Lifeboat,Pclass]]).tolist()[0])

        if y_pred:
            survived = 'sobreviveu'
        else:
            survived = 'morreu'

    return {
	"survived": y_pred,
    "status": 200,
	"message": survived
}


# @app.get('/model')
# def get():
#     return {'hello':'test'}

