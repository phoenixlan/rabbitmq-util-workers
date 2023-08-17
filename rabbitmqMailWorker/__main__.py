import pika
import os
import requests
import json

import logging
logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


MAILGUN_DOMAIN = os.environ["MAILGUN_DOMAIN"]
API_DOMAIN = os.environ["MAILGUN_API"]
API_KEY = os.environ["MAILGUN_API_KEY"]

def callback(ch, method, properties, body):
    log.info("Received %r" % body)
    try:
        requests.post(
            "https://%s/v3/%s/messages" % (API_DOMAIN, MAILGUN_DOMAIN),
            auth=("api", API_KEY),
            data=json.loads(body.decode('utf-8')))

        log.info("Done sending mail")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as err:
        log.warn("Failed to send e-mail: %s" % err)

def main():
    log.info("Starting up mail worker")
    username = os.environ['RABBITMQ_USER']
    password = os.environ['RABBITMQ_PASSWORD']

    credentials = pika.PlainCredentials(username, password)

    connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ.get('RABBITMQ_HOST'), credentials=credentials))
    channel = connection.channel()

    listen_topic = os.environ['RABBITMQ_LISTEN_TOPIC']
    channel.queue_declare(queue=listen_topic, durable=True)

    channel.basic_consume(queue=listen_topic,
                        auto_ack=False,
                        on_message_callback=callback)

    log.info("Listening for events")
    channel.start_consuming()


if __name__ == "__main__":
    main()
