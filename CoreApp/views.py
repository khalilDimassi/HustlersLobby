import json

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'Core/index.html')

