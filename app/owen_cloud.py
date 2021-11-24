import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime


def get_atp(token):
    url = "https://api.owencloud.ru/v1/parameters/last-data"
    headers = CaseInsensitiveDict()
    headers["Host"] = "api.owencloud.ru"
    headers["Accept"] = "*/*"
    headers["Authorization"] = f"Bearer {token}"
    headers["Content-Length"] = "25"
    headers["Content-Type"] = "application/json"

    data = '{"ids":[1123759,1123741,1123749,1123743,1123747,1123757,1123745]}'
    resp = requests.post(url, headers=headers, data=data).json()

    name_param = {"1123759": "запуск/останов контура",
                  "1123741": "датчик аварии насосов (Вх. С5)",
                  "1123749": "авария (Вых. 6)",
                  "1123743": "t наружного воздуха, \N{DEGREE SIGN}C",
                  "1123747": "t подачи, \N{DEGREE SIGN}C",
                  "1123757": "t подачи по графику, \N{DEGREE SIGN}C",
                  "1123745": "t обратки, \N{DEGREE SIGN}C"
                  }

    ts = int(resp[0]['values'][0]['d']) + 7 * 3600
    date_last_update = datetime.utcfromtimestamp(ts).strftime('%d.%m.%Y %H:%M')

    header = f"АТП, г. Барнаул, ул. Г. Исакова, д. 175\n" \
             f"Время последнего обновления параметров: {date_last_update}\n"

    delimit = "---\n"

    pars = []

    for ind in range(len(resp)):
        name = name_param[str(resp[ind]['id'])]
        value = resp[ind]['values'][0]['v']
        pars.append({
            'name': name,
            'value': value
        })

    result = ""

    for params in pars:
        result += f"{params['name']}: {params['value']}\n"

    return header + delimit + result + delimit
