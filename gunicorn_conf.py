import os
from pathlib import Path

# Конфигурация логирования Gunicorn
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = os.path.join(BASE_DIR, "logs/console")
os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(BASE_DIR, "logs/console/console.log")
accesslog = log_file
errorlog = log_file

bind = ":8080"

workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
