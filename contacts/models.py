# -*- coding: utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

#@python_2_unicode_compatible
class Contact(models.Model):
    # Required
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    email = models.EmailField()
    street_address = models.CharField(max_length=300)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=1, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name




