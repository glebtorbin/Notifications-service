FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./notifications ./notifications

CMD [ "python3", "./notifications/manage.py", "runserver", "0.0.0.0:8000"]