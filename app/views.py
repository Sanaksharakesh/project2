from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sanaksha(request):
    return HttpResponse('<h1><marquee> Sahana is a DEVELOPER </marquee></h1>')