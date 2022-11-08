from django.db import models
from django.core import validators as v
from .validators import *
from datetime import date
from django.utils import timezone
from datetime import timedelta


class SwimRecord(models.Model):
    # pass # delete me when you start writing in validations
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=255, validators=[validate_stroke])
    distance = models.IntegerField(validators=[v.MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[validate_record])
    record_broken_date = models.DateTimeField(validators=[validate_record_broken])
    
record = SwimRecord(first_name='j',last_name='j',team_name='k',relay=True,stroke='butterfly',distance=100,record_date=timezone.now(),record_broken_date=(timezone.now() + timedelta(days=1)))
