from django.shortcuts import render
from .models import Song
from .models import Style
from .models import Performance
from .models import Vocalist
from .models import Instrumentalist
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def song(request):
    return render(request, 'song.html')

def style(request):
    Song_list = Song.objects.all()
    Style_list = Style.objects.all()

    if 'id' in request.GET:
        q = request.GET['id']
        F_Song_list = Style.objects.filter(SID=q)[0].song_set.all()
        return render(request, 'style.html', {'Song_list': F_Song_list, 'Style_list': Style_list})

    else:
        return render(request, 'style.html', {'Song_list': Song_list, 'Style_list': Style_list})

def performance(request):
    return render(request, 'performance.html')

def vocalist(request):
    return render(request, 'vocalist.html')

def instrumentalist(request):
    return render(request, 'instrumentalist.html')
