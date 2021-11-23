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
    resp = requests.post(url, headers=headers, data=data)

    name_param = {"1123759": "Запуск/останов контура",
                  "1123741": "Датчик аварии насосов (Вх. С5)",
                  "1123749": "Авария (Вых. 6)",
                  "1123743": "Т наружного воздуха",
                  "1123747": "Т подачи",
                  "1123757": "Т подачи по графику",
                  "1123745": "Т обратки"
                  }

    degree_sign = u"\N{DEGREE SIGN}"
    ts = int(resp.json()[0]['values'][0]['d'])+7*3600
    date_last_update = datetime.utcfromtimestamp(ts).strftime('%d.%m.%Y %H:%M')

    par_00 = name_param[str(resp.json()[0]["id"])]
    par_01 = name_param[str(resp.json()[1]['id'])]
    par_02 = name_param[str(resp.json()[2]['id'])]
    par_03 = name_param[str(resp.json()[3]['id'])]
    par_04 = name_param[str(resp.json()[4]['id'])]
    par_05 = name_param[str(resp.json()[5]['id'])]
    par_06 = name_param[str(resp.json()[6]['id'])]

    par_0 = resp.json()[0]['values'][0]['v']
    par_1 = resp.json()[1]['values'][0]['v']
    par_2 = resp.json()[2]['values'][0]['v']
    par_3 = resp.json()[3]['values'][0]['v']
    par_4 = resp.json()[4]['values'][0]['v']
    par_5 = resp.json()[5]['values'][0]['v']
    par_6 = resp.json()[6]['values'][0]['v']

    return f"АТП, г. Барнаул, ул. Г.Исакова, д. 175\n"\
           f"Время последнего обновления параметров: {date_last_update}\n"\
           f"---\n"\
           f"{par_00}: {par_0}\n"\
           f"{par_01}: {par_1}\n"\
           f"{par_02}: {par_2}\n"\
           f"{par_03}: {par_3}{degree_sign}C\n"\
           f"{par_04}: {par_4}{degree_sign}C\n"\
           f"{par_05}: {par_5}{degree_sign}C\n"\
           f"{par_06}: {par_6}{degree_sign}C\n"\
           f"---\n"
