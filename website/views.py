from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyModel
from .forms import MyForm

# Create your views here.


# def home(request):
#     return HttpResponse("Welcome to the Organizer!")

def index(request):
    data = MyModel.objects.all()

    context = {'data': data}

    return render(request, 'website/index.html', context)


def submit_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Create a new records and put it to the db
            form.save()
            # mymodel = MyModel(
            #     name=form.cleaned_data['name'],
            #     date=form.cleaned_data['ndate'],
            #     is_active=form.cleaned_data['is_active'],
            #     description=form.cleaned_data['description'],
            # )
            # mymodel.save()
            return redirect('message')
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})


def table(request):
    table_data = [
        # Provide the necessary data from the database
        {'id': 1, 'name': 'John Doe', 'date': '2023-07-14', 'is_active': True, 'description': 'Lorem ipsum'}
    ]
    return render(request, 'table.html', {'table_data': table_data})
