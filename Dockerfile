# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.10-slim-bullseye
FROM python:latest 
# 
# EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /home/app

# Create user with group app
RUN groupadd app
RUN useradd -m -g app app -p PASSWORD
RUN usermod -aG app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

# Create "web" directory inside "app" and make it working dir
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . $APP_HOME

# Grant permission for current folder to the user
RUN chown -R app:app $APP_HOME
USER app
