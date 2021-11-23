import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_API_TOKEN']
OWEN_TOKEN = os.environ['OWEN_API_TOKEN']

# webhook settings
WEBHOOK_HOST = 'https://edf4-37-23-44-206.ngrok.io'
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001
