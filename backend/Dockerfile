FROM python:3.8

WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app
RUN pip install pipenv
RUN pipenv install

COPY . /app

EXPOSE 8000
CMD pipenv run python manage.py gunicorn -b 0.0.0.0 -p 8000 -w 1
