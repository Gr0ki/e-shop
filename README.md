## e-shop

![Build Status](https://github.com/Gr0ki/e-shop/actions/workflows/checks.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/Gr0ki/e-shop/badge.svg?branch=main)](https://coveralls.io/github/Gr0ki/e-shop?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## API

[📚 Documentation 📚](https://documenter.getpostman.com/view/22115905/2s7ZE7LPjY)

You can also find more accurate and interactive documentation by running Django server with the instructions below and following the [Documentation page](http://127.0.0.1:8000/api/docs/).

## Install docker-compose
To build and run the project you need to install `docker` and `docker-compose`.

## Build and start the project
```
docker-compose --env-file .dev.env up --build
```