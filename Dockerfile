FROM python:3.7.9-slim

RUN pip install pipenv
WORKDIR /scheduler/

COPY ./src /simulator/
COPY Pipfile /simulator/Pipfile
COPY Pipfile.lock /simulator/Pipfile.lock

RUN pipenv install

CMD ["pipenv", "run", "python3", "main.py"]
