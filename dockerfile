FROM python:3.11-slim-bullseye

RUN python --version \
    pip --version


WORKDIR /code
COPY . /code


RUN pip install -r requirements.txt

ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_PASSWORD

RUN python manage.py makemigrations
RUN python manage.py migrate                      
RUN python manage.py createsuperuser            \
        --noinput                               \
        --email $DJANGO_SUPERUSER_EMAIL         \
        --username $DJANGO_SUPERUSER_USERNAME 

CMD python manage.py runserver 0.0.0.0:8000