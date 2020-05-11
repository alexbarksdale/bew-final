from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponse

from pets.models import Pet


class HomeView(ListView):
    '''Render home page'''
    model = Pet

    def get(self, req):
        return render(req, 'index.html')
