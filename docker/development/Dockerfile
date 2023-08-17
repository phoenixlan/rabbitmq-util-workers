FROM python:3.8

RUN mkdir -p /srv/phoenixMailService && groupadd -r phoenixMailService && useradd -r -g phoenixMailService phoenixMailService; \
chown phoenixMailService:phoenixMailService /srv/phoenixMailService

# TODO this is dumb, should probably not be a common thing. We badly want separate prod and development images
WORKDIR /srv/phoenixMailService
COPY . /srv/phoenixMailService

RUN ls -l; rm -r docker && pip install -e .; rm -r phoenixMailService;

USER phoenixMailService

CMD ["python", "-m", "phoenixMailService"]
