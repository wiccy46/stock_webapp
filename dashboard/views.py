from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html', {})


def prices(request):
    return render(request, 'prices.html', {})


def settings(request):
    return render(request, 'settings.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)