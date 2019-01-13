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
    Song_list = Song.objects.all()
    Style_list = Style.objects.all()
    if 'song' in request.GET:
        q = request.GET['song']
        S_Song_list = Song.objects.filter(SName__icontains=q)|Song.objects.filter(Composer__icontains=q)
        return render(request, 'song.html', {'Song_list': S_Song_list, 'Style_list': Style_list})

    else:
        return render(request, 'song.html', {'Song_list': Song_list, 'Style_list': Style_list})


def style(request):
    Song_list = Song.objects.all()
    Style_list = Style.objects.all()

    if 'id' in request.GET:
        q = request.GET['id']
        F_Song_list = Style.objects.filter(SID=q)[0].song_set.all()
        return render(request, 'style.html', {'Song_list': F_Song_list, 'Style_list': Style_list})

    elif 'id2' in request.GET:
        q = request.GET['id2']
        F_Song_list = Style.objects.filter(SID=q)[0].song_set.all()
        return render(request, 'style.html', {'Song_list': F_Song_list, 'Style_list': Style_list})



    elif 'search' in request.GET:
        q = request.GET['search']
        S_Song_list = Song.objects.filter(SName__icontains=q)|Song.objects.filter(Composer__icontains=q)|Style.objects.filter(SName__icontains=q)[0].song_set.all()
        return render(request, 'style.html', {'Song_list': S_Song_list, 'Style_list': Style_list})

    elif 'song' in request.GET:
         Song.objects.create(SName=request.GET['song'], Language=request.GET['lan'], Composer=request.GET['comp'])
         return render(request, 'style.html', {'Song_list': Song_list, 'Style_list': Style_list})

    else:
        return render(request, 'style.html', {'Song_list': Song_list, 'Style_list': Style_list})

def performance(request):
    return render(request, 'performance.html')

def vocalist(request):
    return render(request, 'vocalist.html')

def instrumentalist(request):
    return render(request, 'instrumentalist.html')
