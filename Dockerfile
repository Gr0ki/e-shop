# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.8-slim
# FROM python:3.10-slim-bullseye
FROM python:latest 

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


WORKDIR /e-shop
COPY . /e-shop

# Update .env file with Django SECRET_KEY
RUN python -c 'from django.core.management.utils import get_random_secret_key; print(f"export SECRET_KEY=\"{get_random_secret_key()}\"")' >> .env

# Creates a non-root user with an explicit UID and adds permission to access the /e-shop folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /e-shop
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
