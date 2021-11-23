FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY .env .
COPY owen_cloud.py .

CMD [ "python3.8", "./main.py" ]
