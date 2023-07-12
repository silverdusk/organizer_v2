from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

# Create your views here.


def home(request):
    return HttpResponse("Welcome to the Organizer!")

def index(request):
    data = MyModel.objects.all()

    context = {'data': data}

    return render(request, 'website/index.html', context)