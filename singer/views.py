from django.shortcuts import render
from .models import Song
from .models import Style
from .models import Performance
from .models import Vocalist
from .models import Instrumentalist

# Create your views here.

def home(request):
    return render(request, 'home.html')

def song(request):
    return render(request, 'song.html')

def style(request):
    return render(request, 'style.html')

def performance(request):
    return render(request, 'performance.html')

def vocalist(request):
    return render(request, 'vocalist.html')

def instrumentalist(request):
    return render(request, 'instrumentalist.html')