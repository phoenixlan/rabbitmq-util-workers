FROM python:3.8

RUN mkdir -p /srv/rabbitmqUtilWorkers && groupadd -r rabbitmqUtilWorkers && useradd -r -g rabbitmqUtilWorkers rabbitmqUtilWorkers; \
chown rabbitmqUtilWorkers:rabbitmqUtilWorkers /srv/rabbitmqUtilWorkers

# TODO this is dumb, should probably not be a common thing. We badly want separate prod and development images
WORKDIR /srv/rabbitmqUtilWorkers
COPY . /srv/rabbitmqUtilWorkers

RUN ls -l; rm -r docker && pip install -e .; rm -r rabbitmqUtilWorkers;

USER rabbitmqUtilWorkers

CMD ["python", "-m", "rabbitmqUtilWorkers.mailWorker"]
