# celery_schedule_project/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelerybeat.settings')

app = Celery('djcelerybeat')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
