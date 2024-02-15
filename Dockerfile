FROM --platform=linux/amd64 python:3.9-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.2

# System deps:
RUN pip install "poetry==$POETRY_VERSION"
# RUN apt-get update -y
# RUN apt-get install libgraphviz-dev -y

# Copy only requirements to cache them in docker layer
RUN mkdir app
WORKDIR /app
# COPY poetry.lock pyproject.toml /app/
COPY pyproject.toml /app/

ENV PYTHON_KEYRING_BACKEND keyring.backends.null.Keyring
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENTRYPOINT ["python", "-m", "model"]
