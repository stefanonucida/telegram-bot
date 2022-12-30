FROM python:3.8

RUN pip install requests
RUN pip install python-telegram-bot --pre

COPY . /app
WORKDIR /app

CMD ["python", "bot.py"]
