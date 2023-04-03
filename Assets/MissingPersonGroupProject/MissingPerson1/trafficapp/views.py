from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'trafficapp/index.html')

def aboutPageView(request):
    return render(request, 'trafficapp/about.html')

def MissingpeoplePageView(request):
    return render(request, 'trafficapp/missingpeople.html')

def ContactPageView(request):
    return render(request, 'trafficapp/contact.html')