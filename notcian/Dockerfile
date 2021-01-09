FROM python:3.8

WORKDIR /user

RUN apt-get update

RUN apt-get install -y default-libmysqlclient-dev

RUN pip install django uwsgi mysqlclient pillow

COPY . /user

EXPOSE 8002

CMD ["uwsgi", "--socket", "0.0.0.0:8002", "--module", "notcian.wsgi"]



