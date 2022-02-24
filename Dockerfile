# choose an image -> what version of linux wer waant
FROM python:3.8-buster

# put in our container all the code we need

COPY simple.py /simple.py
COPY requirements.txt /requirements.txt
COPY best_model.joblib /best_model.joblib

#install on our container pip and all the packages we need
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#we will ask our container to launch a web server with uvicorn
CMD uvicorn simple:app --host 0.0.0.0 --port $PORT
