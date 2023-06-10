FROM python:3.11.1-alpine3.17

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN addgroup -S backend-group && \
    adduser -S backend-user -G backend-group && \
    mkdir -p /home/backend-user/app/coverage && \
    mkdir -p /home/backend-user/app/static


COPY ./dockerfiles/django/requirements/requirements.txt /tmp/requirements.txt
COPY ./dockerfiles/django/requirements/dev.requirements.txt /tmp/dev.requirements.txt

COPY ./dockerfiles/django/requirements/pytest.ini /home/backend-user/app/pytest.ini
COPY ./dockerfiles/django/requirements/.pylintrc /home/backend-user/app/.pylintrc
COPY ./dockerfiles/django/requirements/.coveragerc /home/backend-user/app/.coveragerc

COPY ./.git /home/backend-user/app/.git


WORKDIR /home/backend-user/app

EXPOSE 8000

ARG DEV=${DEV}

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    apk add git && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /venv/bin/pip install -r /tmp/dev.requirements.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    chown -R backend-user:backend-group /home/backend-user/app

ENV PATH="/venv/bin:$PATH"

USER backend-user
