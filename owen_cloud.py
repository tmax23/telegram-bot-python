import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime
"""
0 Запуск/останов контура - "id": 1123759
1 Датчик аварии насосов (Вх. С5) - "id": 1123741
2 Авария (Вых. 6) - "id": 1123749
3 Т наружного воздуха  - "id": 1123743
4 Т подачи - "id": 1123747
5 Т подачи по графику - "id": 1123757
6 Т обратки - "id": 1123745
"""


def get_temperature(token):
    url = "https://api.owencloud.ru/v1/parameters/last-data"
    headers = CaseInsensitiveDict()
    headers["Host"] = "api.owencloud.ru"
    headers["Accept"] = "*/*"
    headers["Authorization"] = f"Bearer {token}"
    headers["Content-Length"] = "25"
    headers["Content-Type"] = "application/json"

    data = '{"ids":[1123759,1123741,1123749,1123743,1123747,1123757,1123745]}'
    resp = requests.post(url, headers=headers, data=data)

    ts = int(resp.json()[0]['values'][0]['d'])+25200
    date_last_update = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    par_0 = resp.json()[0]['values'][0]['v']
    par_1 = resp.json()[1]['values'][0]['v']
    par_2 = resp.json()[2]['values'][0]['v']
    par_3 = resp.json()[3]['values'][0]['v']
    par_4 = resp.json()[4]['values'][0]['v']
    par_5 = resp.json()[5]['values'][0]['v']
    par_6 = resp.json()[6]['values'][0]['v']

    degree_sign = u"\N{DEGREE SIGN}"

    return f"My ATP, Barnaul, G. Isakova 175:\n" f"Time of last parameters update: {date_last_update}\n" f"---\n" f"Запуск/останов контура: {par_0}\n" f"Датчик аварии насосов (Вх. С5): {par_1}\n" f"Авария (Вых. 6): {par_2}\n" f"Т наружного воздуха: {par_3}{degree_sign}C\n" f"Т подачи: {par_4}{degree_sign}C\n" f"Т подачи по графику: {par_5}{degree_sign}C\n" f"Т обратки: {par_6}{degree_sign}C\n" f"---\n"
