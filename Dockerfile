FROM python:3.11
WORKDIR /app
COPY pyproject.toml poetry.lock alembic.ini ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY run.py .
COPY src ./src
CMD ["python3", "run.py"]