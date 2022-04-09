from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data


# Create your views here.
def index(request):
    if request.method == 'POST':
        forms = DataForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('predict')

    else:
        forms = DataForm()
        context = {
            'forms' : forms
        }

    return render(request, 'predictions/index.html', context)



def prediction(request): 

    predicted_sport = Data.objects.all()

    context = {
        'predicted_sport' : predicted_sport
    }

    return render(request, 'predictions/predict.html', context)
