import pickle
from fastapi import FastAPI,Response, status
import os

app = FastAPI()

@app.post('/model',status_code=200)
## Coloque seu codigo na função abaixo
async def titanic(Sex:int,Age:float,Lifeboat: int,Pclass:int,response: Response):
    with open('Titanic.pkl', 'rb') as fid: 
    
        titanic = pickle.load(fid)
        
        response.status_code = status.HTTP_201_CREATED
    return {
	"survived": bool(titanic.predict([[Sex,Age,Lifeboat,Pclass]])),
    "status": response.status_code,
	"message": "Me Contrata Stefanini!! :)"
}


@app.get('/model')
def get():
    return {'hello':'test'}

