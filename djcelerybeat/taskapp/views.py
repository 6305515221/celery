# taskapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import datetime
import json
from taskapp.tasks import send_fake_report
class ScheduleReportView(APIView):
    def post(self, request):
        # Default values or fetch from request
        every = request.data.get("every", 1)
        period = request.data.get("period", "minutes").upper()

        # Create or get interval schedule
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=int(every),
            period=period,
        )

        # Generate a unique name using timestamp
        name = f"send_report_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Create the periodic task
        PeriodicTask.objects.create(
            interval=schedule,
            name=name,
            task=send_fake_report,
            args=json.dumps([]),
            
        )

        return Response(
            {"message": f"Scheduled '{name}' every {every} {period.lower()}."},
            status=status.HTTP_201_CREATED
        )
