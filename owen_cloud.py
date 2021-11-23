import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime


def get_temperature():
    url = "https://api.owencloud.ru/v1/parameters/last-data"
    headers = CaseInsensitiveDict()
    headers["Host"] = "api.owencloud.ru"
    headers["Accept"] = "*/*"
    headers["Authorization"] = "Bearer mMwNjU3NDM5ZWJkOTZlMGE1O"
    headers["Content-Length"] = "25"
    headers["Content-Type"] = "application/json"

    data = '{"ids":[1123743]}'

    resp = requests.post(url, headers=headers, data=data)

    ts = int(resp.json()[0]['values'][0]['d'])+25200
    temperature_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    temperature = resp.json()[0]['values'][0]['v']

    return f"{temperature_date}: temperature is {temperature}"
