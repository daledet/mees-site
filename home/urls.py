from django.urls import path
from . import views
from .views import HomeView, PastEventView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', PastEventView.as_view(), name='events'),
    path('about/', AboutView.as_view(), name='about'),
]
