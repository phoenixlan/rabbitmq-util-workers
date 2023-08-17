FROM python:3.8-alpine

RUN mkdir -p /srv/phoenixMailService && addgroup -S phoenixMailService && adduser -S phoenixMailService -G phoenixMailService; \
chown phoenixMailService:phoenixMailService /srv/phoenixMailService;

WORKDIR /srv/phoenixMailService
COPY . /srv/phoenixMailService

RUN pip install -e .

USER phoenixMailService

CMD ["python", "-m", "phoenixMailService"]