import os

import requests
from dotenv import load_dotenv

load_dotenv()

jwt_token = os.getenv('jwt_token')
refresh_token = os.getenv('jwt_refresh')


def format_result(result):
    output = ''
    for item in result:
        text = item['text']
        date = item['date']
        status = item['status']
        line = (
            f'Кейс: {text}\n'
            f'<code>Дата: {date}</code>\n'
            f'Статус: <b>{status}</b>\n '
            '\n'
        )
        output += line
    return output


def show_all(message, bot):
    reports_status = str(message.text)
    reports = requests.get(
        url=f'http://127.0.0.1:8000/api/v1/report/?status={reports_status}',
        headers={
            'Authorization': f'Bearer {jwt_token}',
        }
    )
    result = reports.json()
    output = format_result(result)
    bot.send_message(
        message.from_user.id,
        output,
        parse_mode='HTML',
    )
