#!/usr/bin/env bash
set -e

# Создание директории кэша, если она еще не существует
mkdir -p /pip-cache

# Установка Poetry
pip install --upgrade pip
pip install poetry
export PATH="/root/.local/bin:$PATH"

# Настройка Poetry для использования кэша
poetry lock --no-update

poetry config virtualenvs.create false
poetry config cache-dir /pip-cache
pip install --upgrade pip wheel fpdf
PIP_NO_BINARY="psycopg2"
poetry install --no-root
