from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class Profile(models.Model):
    """
    A user profile model for maintaining contact info and timezone info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    timezone = models.CharField(max_length=50, choices=TIMEZONES, default='UTC')
    reminders = models.BooleanField()
    
    def __str__(self):
        return self.user.username
