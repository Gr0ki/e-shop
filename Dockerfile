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
