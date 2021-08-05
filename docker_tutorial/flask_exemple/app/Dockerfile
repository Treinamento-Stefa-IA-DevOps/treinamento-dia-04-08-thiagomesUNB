FROM python:3.8-slim  
# imagem base

COPY . /app  
# copia tudo dentro do contexto para o diretorio /app dentro do container

WORKDIR /app  
# seta o /app como diretorio base

RUN pip install flask  
# instala as dependencias do python

ENV FLASK_APP=flask_app.py  
# requerimento para rodar o flask run

CMD ["flask", "run", "--host","0.0.0.0", "--port","5000"]  
# comando rodado ao iniciar o container
