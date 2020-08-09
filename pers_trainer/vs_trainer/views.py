from django.http import HttpResponse
from django.shortcuts import render
from .models import services, portfolio

def index(request):

    srv = services.objects.all()
    prt = portfolio.objects.all()

    return render(request, 'index.html', {'srv':srv, 'prt':prt})