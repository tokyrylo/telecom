PROJECT_NAME := $(shell basename $(CURDIR))

DOCKER_COMPOSE := docker-compose
DC_RUN := $(DOCKER_COMPOSE) run --rm app

.PHONY: build up down restart logs bash sh migrate

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

restart: down up

logs:
	$(DOCKER_COMPOSE) logs -f

bash:
	$(DOCKER_COMPOSE) exec app /bin/bash || $(DOCKER_COMPOSE) exec app /bin/sh

migrate:
	$(DC_RUN) alembic upgrade head
