# taskapp/urls.py
from django.urls import path
from .views import ScheduleReportView

urlpatterns = [
    path('schedule-task/', ScheduleReportView.as_view()),
]
