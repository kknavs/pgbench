#za vstavitev podatkov v db

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from submitted_measurement.models import SubmittedMeasurement
from decimal import *
from django.utils import timezone
import os


class Command(BaseCommand):
    def handle(self, name, *args, **kwargs):
        path = "pgbench/static"
        root = os.getcwd()
        os.chdir(path)
        content = open(name)
        os.chdir(root)
        user = User.objects.filter(username="admin")[0]
        for line in content:
            if line[0] == ";":
                continue
            if line in ["\n"]:
                continue
            line = line[:-1]
            title, tags, transactionType, scalingFactor, threads, clients, transactionsPerClient, \
                transactions, TPS, TPSConnEstablish = line.split(
                    ";")
            s = SubmittedMeasurement()
            s.date = timezone.localtime(timezone.now())
            s.title = title
            s.tags = tags
            s.transactionType = transactionType
            if scalingFactor != '':
                if "," in scalingFactor:
                    scalingFactor = scalingFactor.replace(",", ".")
                s.scalingFactor = Decimal(scalingFactor)
            if threads != '':
                s.threads = int(threads)
            if clients != '':
                s.clients = clients
            if transactionsPerClient != '':
                s.transactionsPerClient = int(transactionsPerClient)
            if transactions != '':
                s.transactions = int(transactions)
            if TPS != '':
                s.TPS = int(TPS)
            s.TPSConnEstablish = int(TPSConnEstablish)
            s.user = user
            s.save()
            print "Added measurement: "+s.title