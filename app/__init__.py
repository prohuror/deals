# Импорт Celery, загружается при запуске Django
from .celery import app as celery_app

__all__ = ['celery_app']