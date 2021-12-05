FROM python:3.8

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt && chmod +x start_api.sh

COPY . /app
WORKDIR /app

ENTRYPOINT ./start_api.sh
