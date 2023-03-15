from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a': 190,'b': 300,'c': 2000}
    return render(request,'conditions.html',d)
