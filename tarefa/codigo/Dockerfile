#FROM python:3.8-slim
FROM centos/python-36-centos7

RUN pip install pandas
RUN pip install sklearn
RUN pip3 install fastapi uvicorn

COPY . /codigo 

WORKDIR /codigo 

EXPOSE 80

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0","--port", "80","--reload"]
