import environ
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()

for i in ("../", "./"):
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), i, ".env"))
    if os.path.exists(path):
        env.read_env(path)
