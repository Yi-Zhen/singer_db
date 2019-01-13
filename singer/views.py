from django.shortcuts import render
from .models import Song
from .models import Style
from .models import Performance
from .models import Vocalist
from .models import Instrumentalist

# Create your views here.

def home(request):
    Song_list = Song.objects.all()
    return render(request, 'home.html', {'Song_list': Song_list,})