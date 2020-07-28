from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Django rest framework with react',
    }
    return render(request, 'frontend/index.html', context)
