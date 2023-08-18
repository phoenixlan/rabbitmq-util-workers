FROM python:3.8-alpine

RUN mkdir -p /srv/rabbitmqUtilWorkers && addgroup -S rabbitmqUtilWorkers && adduser -S rabbitmqUtilWorkers -G rabbitmqUtilWorkers; \
chown rabbitmqUtilWorkers:rabbitmqUtilWorkers /srv/rabbitmqUtilWorkers;

WORKDIR /srv/rabbitmqUtilWorkers
COPY . /srv/rabbitmqUtilWorkers

RUN pip install -e .

USER rabbitmqUtilWorkers

CMD ["python", "-m", "rabbitmqUtilWorkers.mailWorker"]