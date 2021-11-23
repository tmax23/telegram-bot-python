FROM python:3.8

WORKDIR /usr/src/app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD app/ .

CMD [ "python3.8", "./main.py" ]
