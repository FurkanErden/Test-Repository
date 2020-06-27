FROM python:3.7.3

WORKDIR /app
ADD . /app

CMD [ "python3", "/app/code_1.py" ]
