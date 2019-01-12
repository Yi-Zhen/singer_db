from django.contrib import admin
from .models import Song
from .models import Style
from .models import Performance
from .models import Vocalist
from .models import Instrumentalist

admin.site.register(Song)
admin.site.register(Style)
admin.site.register(Performance)
admin.site.register(Vocalist)
admin.site.register(Instrumentalist)