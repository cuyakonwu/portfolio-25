FROM python:3.9-slim-buster

WORKDIR /MLH-Portfolio

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

EXPOSE 5000