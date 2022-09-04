# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.10-slim-bullseye
FROM python:latest 

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /e-shop
COPY . /e-shop

# Install requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


# TODO: Hide envs:
# write SECRET_KEY to the ./django_secrets.env for django
# RUN export SECRET="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
# ENV DB_HOST=db
# ENV DB_PORT=5432
# ENV DB_NAME=psql_db_dev
# ENV DB_USER=admin
# ENV DB_PASS=t0hOid24n2sdlL22I

# Creates a non-root user with an explicit UID and adds permission to access the /e-shop folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

# TODO: Manage user creation for security purposes
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /e-shop
# USER appuser

# RUN adduser -D appuser && chown -R appuser /e-shop
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# RUN python manage.py makemigrations && python manage.py migrate
# CMD ["python", "manage.py", "runserver", "0:8000"]
