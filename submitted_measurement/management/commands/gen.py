#za generiranje testnih vnosov v db

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from submitted_measurement.models import SubmittedMeasurement
from datetime import datetime
from django.utils import timezone
import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(int(args[0])):
            s = SubmittedMeasurement()
            s.date = timezone.localtime(timezone.now())
            s.title = "test" + str(i+1)
            s.TPSConnEstablish = random.randrange(1000, 5000)
            s.user = User.objects.filter(username="admin")[0]
            s.threads = random.randrange(1, 20)
            s.scalingFactor = random.uniform(1, 5)
            s.clients = random.randrange(200, 3000)
            s.transactionsPerClient = random.randrange(5, 100)
            s.transactions = random.randrange(5000, 100000)
            s.TPS = random.randrange(1000, 100000)
            s.save()
