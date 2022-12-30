FROM python:3.8-slim

RUN pip install python-telegram-bot requests

COPY . /app
WORKDIR /app

CMD ["python", "bot.py"]
