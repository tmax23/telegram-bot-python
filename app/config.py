import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_API_TOKEN']
OWEN_TOKEN = os.environ['OWEN_API_TOKEN']
EXT_IP = os.environ['EC2_IP_ADDRESS']
ENV = os.environ['ENV']

# webhook settings
if ENV == "dev":
    WEBHOOK_HOST = 'https://203f-95-167-217-2.ngrok.io'
else:
    WEBHOOK_HOST = EXT_IP

WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
if ENV == "dev":
    WEBAPP_HOST = 'localhost'
else:
    WEBAPP_HOST = 'tg-bot-py'

WEBAPP_PORT = 3001
