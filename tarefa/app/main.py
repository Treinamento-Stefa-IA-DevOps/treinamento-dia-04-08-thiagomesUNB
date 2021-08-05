import pickle
from fastapi import FastAPI
import os

app = FastAPI()

@app.post('/model')
## Coloque seu codigo na função abaixo
async def titanic(Sex:int,Age:float,Lifeboat: int,Pclass:int):
    with open('Titanic.pkl', 'rb') as fid: 
    
        titanic = pickle.load(fid)
        titanic.predict([[Sex,Age,Lifeboat,Pclass]])
        
    return {
	"survived": bool(titanic.predict([[Sex,Age,Lifeboat,Pclass]])),	
	"message": "teste"
}


@app.get('/model')
def get():
    return {'hello':'test'}

