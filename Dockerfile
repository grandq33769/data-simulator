FROM python:3.7.9-slim

RUN pip install pipenv
WORKDIR /

COPY ./src /src/
COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

RUN pipenv install

CMD ["pipenv", "run", "python3", "-m", "src.main"]
