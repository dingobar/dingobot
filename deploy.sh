#!/usr/bin/env bash

poetry run sam build --use-container
poetry run sam deploy --confirm-changeset