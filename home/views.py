from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import NewsLetter, Event, PastEvent, About


class HomeView(ListView):
    paginate_by = 1
    model = NewsLetter
    template_name = 'home.html'
    ordering = ['-post_date']

    def events(self):
        return Event.objects.order_by('event_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Today'] = timezone.now().date()
        return context


class PastEventView(ListView):
    model = PastEvent
    template_name = 'events.html'
    ordering = ['-order_date']


class AboutView(ListView):
    model = About
    template_name = 'about.html'


# def home(request):
#     return render(request, 'home.html', {})
