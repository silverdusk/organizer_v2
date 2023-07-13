from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

# Create your views here.


# def home(request):
#     return HttpResponse("Welcome to the Organizer!")

def index(request):
    data = MyModel.objects.all()

    context = {'data': data}

    return render(request, 'website/index.html', context)

def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})