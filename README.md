# Rabbitmq util workers

A collection of utility workers that are useful when you don't want to do common stuff in your webserver thread.

## Features

 * Mail service for use with rabbitmq. Listens to a specific topic and sends e-mails.

## Configuration

The following environment variables can be configured:

 * `RABBITMQ_LISTEN_TOPIC` - Topic to listen to
 * `RABBITMQ_HOST` - Host of the rabbitmq server
