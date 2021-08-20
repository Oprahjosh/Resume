from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'Resume/index.html', {})

def success(request):
    return render(request, 'Resume/success.html', {})