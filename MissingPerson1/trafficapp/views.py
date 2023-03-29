from django.shortcuts import render

from django.http import HttpResponse

def indexPageView(request):
    return render(request, 'trafficapp/index.html')
# Create your views here.
