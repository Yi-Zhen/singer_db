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

    elif 'sName' in request.GET:
         nsong = Song.objects.create(SName=request.GET['sName'], Language=request.GET['lan'], Composer=request.GET['comp'])
         if 'nstyle' in request.GET:
             q = request.GET['nstyle']
             try:
                 ostyle = Style.objects.get(SName=q)
             except Style.DoesNotExist:
                 ostyle = Style.objects.create(SName=q)
             ostyle.song_set.add(nsong)

         if 'voc' in request.GET:
             q = request.GET['voc']
             try:
                 voc = Vocalist.objects.get(VName=q)
             except Vocalist.DoesNotExist:
                 voc = Vocalist.objects.create(VName=q)

             nsong.vocalist_set.add(voc)

         return render(request, 'song.html', {'Song_list': Song_list, 'Style_list': Style_list})

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
        S_Song_list = Song.objects.filter(SName__icontains=q)|Song.objects.filter(Composer__icontains=q)#|Style.objects.filter(SName__icontains=q)[0].song_set.all()
        return render(request, 'style.html', {'Song_list': S_Song_list, 'Style_list': Style_list})

    elif 'song' in request.GET:
         Song.objects.create(SName=request.GET['song'], Language=request.GET['lan'], Composer=request.GET['comp'])
         return render(request, 'style.html', {'Song_list': Song_list, 'Style_list': Style_list})

    else:
        return render(request, 'style.html', {'Song_list': Song_list, 'Style_list': Style_list})

def performance(request):
    Per_list = Performance.objects.all()
    if 'search' in request.GET:
        q = request.GET['search']
        S_Song_list = Performance.objects.filter(PName__icontains=q)|Performance.objects.filter(Company__icontains=q)|Performance.objects.filter(Venue__icontains=q)|Performance.objects.filter(Equipment__icontains=q)
        return render(request, 'performance.html', {'Per_list': S_Song_list})

    else:
        return render(request, 'performance.html', {'Per_list': Per_list})

def vocalist(request):
    Voc_list = Vocalist.objects.all()
    if 'search' in request.GET:
        q = request.GET['search']
        S_Song_list = Vocalist.objects.filter(VName__icontains=q)|Vocalist.objects.filter(Gender__icontains=q)|Vocalist.objects.filter(Vocal_Range__icontains=q)|Vocalist.objects.filter(Vocal_Type__icontains=q)|Vocalist.objects.filter(Language__icontains=q)|Vocalist.objects.filter(Music_Training__icontains=q)
        return render(request, 'vocalist.html', {'Voc_list': S_Song_list})

    else:
        return render(request, 'vocalist.html', {'Voc_list': Voc_list})

    

def instrumentalist(request):
    return render(request, 'instrumentalist.html')
