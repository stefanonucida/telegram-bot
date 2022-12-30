FROM arm64v8/python

RUN pip install python-telegram-bot requests

COPY . /app
WORKDIR /app

CMD ["python", "bot.py"]
