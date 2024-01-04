# base image
# FROM jumpserver/python:3.12-slim
FROM python:3.11.6-alpine3.17


# enviroment variable
ENV APP /k9


# working directory
WORKDIR $APP


# copy our project
COPY . .


RUN pip install -r requirements.txt


ENTRYPOINT ["python", "main.py"]
