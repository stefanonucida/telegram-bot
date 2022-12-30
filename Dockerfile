FROM python:3.8

RUN pip install python-telegram-bot 
RUN pip install requests

COPY . /app
WORKDIR /app

CMD ["python", "bot.py"]
