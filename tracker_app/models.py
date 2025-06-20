from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cycle_length = models.IntegerField(default=28)  # days
    period_length = models.IntegerField(default=5)  # days
    last_period_start_date = models.DateField()

    def next_period_start_date(self):
        return self.last_period_start_date + timedelta(days=self.cycle_length)

    def ovulation_start_date(self):
        ovulation_day = self.cycle_length - 14
        return self.last_period_start_date + timedelta(days=ovulation_day)

class PeriodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

class SymptomLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    symptom = models.CharField(max_length=100)
    intensity = models.IntegerField()  # 1-5
    notes = models.TextField(blank=True, null=True)
