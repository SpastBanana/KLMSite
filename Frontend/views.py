from django.shortcuts import render
from django.contrib.auth.models import User

def startView(request):
    template_name = 'start.html'
    return render(request, 'index.html', {'page': template_name})

def dashboardView(request):
    template_name = 'dashboard.html'
    return render(request, 'index.html', {'page': template_name})

def systemView(request):
    template_name = 'system.html'
    return render(request, 'index.html', {'page': template_name})
