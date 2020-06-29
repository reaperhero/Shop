from django.http import HttpResponse
from django.shortcuts import render
from .models import Types

# Create your views here.


def loadinfo(request):
    context = {}
    context['types'] = Types.objects.all()
    return context

