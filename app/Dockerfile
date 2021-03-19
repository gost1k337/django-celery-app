FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependecies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* /usr/src/app/
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt


COPY . /usr/src/app/
