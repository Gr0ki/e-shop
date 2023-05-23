FROM python:3.11.1-alpine3.17

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/coverage && \
    addgroup -S backend-group && \
    adduser -S backend-user -G backend-group


COPY ./dockerfiles/django/requirements/requirements.txt /tmp/requirements.txt
COPY ./dockerfiles/django/requirements/dev.requirements.txt /tmp/dev.requirements.txt

COPY ./dockerfiles/django/requirements/pytest.ini /app/pytest.ini
COPY ./dockerfiles/django/requirements/.pylintrc /app/.pylintrc

COPY ./.git /app/.git


WORKDIR /app

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
    chown -R backend-user:backend-group /app

ENV PATH="/venv/bin:$PATH"

USER backend-user
