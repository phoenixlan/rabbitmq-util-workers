FROM python:3.8-alpine

RUN mkdir -p /srv/rabbitmqMailWorker && addgroup -S rabbitmqMailWorker && adduser -S rabbitmqMailWorker -G rabbitmqMailWorker; \
chown rabbitmqMailWorker:rabbitmqMailWorker /srv/rabbitmqMailWorker;

WORKDIR /srv/rabbitmqMailWorker
COPY . /srv/rabbitmqMailWorker

RUN pip install -e .

USER rabbitmqMailWorker

CMD ["python", "-m", "rabbitmqMailWorker"]