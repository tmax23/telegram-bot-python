import logging
import os
from dotenv import load_dotenv

import owen_cloud

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

load_dotenv()

API_TOKEN = os.environ['ENV_API_TOKEN']

# webhook settings
WEBHOOK_HOST = 'https://3.143.4.211'
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'tg-bot-py'  # or ip
WEBAPP_PORT = 3001

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


# @dp.message_handler()
# async def echo(message: types.Message):
#     # Regular request
#     # await bot.send_message(message.chat.id, message.text)
#
#     # or reply INTO webhook
#     return SendMessage(message.chat.id, message.text)


@dp.message_handler(commands='myatp')
async def create_deeplink(message: types.Message):
    data = owen_cloud.get_temperature()
    return SendMessage(message.chat.id, data)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
