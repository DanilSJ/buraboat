#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def create_media_folders():
    # Создаем папку media, если её нет
    media_root = os.path.join(os.getcwd(), 'media')
    if not os.path.exists(media_root):
        os.mkdir(media_root)
    
    # Создаем папку qr внутри папки media, если её нет
    qr_folder = os.path.join(media_root, 'qr')
    if not os.path.exists(qr_folder):
        os.mkdir(qr_folder)
        
    # Создаем папку pdf внутри папки media, если её нет
    pdf_folder = os.path.join(media_root, 'pdf')
    if not os.path.exists(pdf_folder):
        os.mkdir(pdf_folder)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boraboat.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    create_media_folders()  # Создаем папки media и qr перед запуском проекта

    execute_from_command_line(sys.argv)  # Запускаем Django-команду

if __name__ == '__main__':
    main()
