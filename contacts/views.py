# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


#Create a login page
def login(request):
    return HttpResponse("This will be the login page")



# Create your views here.
