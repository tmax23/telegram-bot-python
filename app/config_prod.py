import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_API_TOKEN']
OWEN_TOKEN = os.environ['OWEN_API_TOKEN']
EXT_IP = os.environ['EC2_IP_ADDRESS']

# webhook settings
WEBHOOK_HOST = EXT_IP
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'tg-bot-py'
WEBAPP_PORT = 3001