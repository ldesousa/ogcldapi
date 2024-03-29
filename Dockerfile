FROM python:3.7-slim-buster

EXPOSE 9000

COPY ./app ./
RUN apt -y update
RUN apt install -y git
RUN pip install -r ./requirements.txt

CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "9000"]
#docker build -t ogc-api . -f Dockerfile
#docker run -p 9000:9000 --env-file .env -it --name ogc-api ogc-api
