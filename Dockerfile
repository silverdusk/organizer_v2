FROM python:3.8-slim-buster

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY organizer_v2 /app/organizer_v2

CMD ["poetry", "run", "python", "organizer_v2/manage.py", "runserver", "0.0.0.0:8000"]
