# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact
import datetime



class ContactListInfo(admin.ModelAdmin):
    # fieldsets = [
    #     ('Contact Information',   {'fields':['first_name', 'last_name', 'phone_number']}),
    #     ('Birthday Reminders',    {'fields':['birthday_reminder']})
    # ]
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'phone_number','dob']
    list_filter = ['last_name']

admin.site.register(Contact,ContactListInfo)



