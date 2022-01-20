FROM python:3.9-slim AS builder
WORKDIR /root
COPY pyproject.toml ./
RUN pip install setuptools -U && \
    pip install --upgrade pip && \
    pip install --no-cache-dir poetry==1.1.* && \
    poetry export --without-hashes -f requirements.txt -o requirements.txt && \
    poetry export --dev --without-hashes -f requirements.txt -o requirements-dev.txt


FROM python:3.9-slim AS prd
WORKDIR /root
COPY --from=builder /root/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY ./app ./app

CMD exec uvicorn --port $PORT --host 0.0.0.0 app.main:app


FROM python:3.9-slim AS dev
WORKDIR /root
COPY --from=builder /root/requirements-dev.txt /tmp
RUN pip install -r /tmp/requirements-dev.txt
COPY ./app ./app

CMD exec uvicorn --port $PORT --host 0.0.0.0 app.main:app
