FROM python:3.7.3

RUN mkdir /app
WORKDIR /app

ADD . /app/

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 8000

RUN ./manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000