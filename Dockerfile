FROM python:3.8-slim-buster

WORKDIR ~/secure-python-flask-api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
RUN "python3 -m venv /env/"
RUN "source env/bin/activate"
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]

