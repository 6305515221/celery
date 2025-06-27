# taskapp/tasks.py
from celery import shared_task
import datetime

@shared_task
def send_fake_report():
    print("📝 Report sent at", datetime.datetime.now())

# @shared_task
# @shared_task
# def send_fake_report2():
#     print("📝 Report sent at", datetime.datetime.now())
