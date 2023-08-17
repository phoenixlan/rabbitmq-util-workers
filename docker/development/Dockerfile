FROM python:3.8

RUN mkdir -p /srv/rabbitmqMailWorker && groupadd -r rabbitmqMailWorker && useradd -r -g rabbitmqMailWorker rabbitmqMailWorker; \
chown rabbitmqMailWorker:rabbitmqMailWorker /srv/rabbitmqMailWorker

# TODO this is dumb, should probably not be a common thing. We badly want separate prod and development images
WORKDIR /srv/rabbitmqMailWorker
COPY . /srv/rabbitmqMailWorker

RUN ls -l; rm -r docker && pip install -e .; rm -r rabbitmqMailWorker;

USER rabbitmqMailWorker

CMD ["python", "-m", "rabbitmqMailWorker"]
