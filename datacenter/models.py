from datetime import datetime, timedelta

import pytz
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(visit):
        entered_at = visit.entered_at
        leaved_at = visit.leaved_at
        now = datetime.now(pytz.timezone('Europe/Moscow'))
        if leaved_at:
            delta = leaved_at - entered_at
        else:
            delta = now - entered_at
        return delta

    def format_duration(delta):
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours} часов, {minutes} минут, {seconds} секунд"

    def format_time_in_minutes(delta):
        minutes = delta.total_seconds() // 60
        return minutes
    def is_visit_long(visit, minutes=60):
        leaved_at = visit.leaved_at
        delta = Visit.get_duration(visit)
        if not leaved_at and delta < timedelta(minutes=minutes):
            return False
        if delta < timedelta(minutes=minutes):
            return False
        duration = Visit.get_duration(visit)
        visit_time = Visit.format_time_in_minutes(duration)
        if visit_time > minutes:
            return True
        return False



    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
