# pull official base image
FROM python:3.8.0-alpine
FROM postgres:14.1

RUN apt-get update && apt-get  install -y postgresql-14-postgis-3 
# set work directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# copy project
COPY . /app
# install dependencies
RUN pip install --upgrade pip
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "src/build.py"]
# RUN ls -la app/
# ENTRYPOINT ["app/app/docker-entrypoint.sh"]