from django.contrib import admin
from . models import NewsLetter, Event, PastEvent, About

admin.site.register(NewsLetter)
admin.site.register(Event)
admin.site.register(PastEvent)
admin.site.register(About)
