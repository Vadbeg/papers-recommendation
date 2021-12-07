FROM python:3.8

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app
RUN chmod +x start_api.sh

#ENTRYPOINT uvicorn papers_recommendation.api.api:app --reload --port 8000 --host 0.0.0.0
ENTRYPOINT ["bash"]
