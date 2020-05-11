from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse

from pets.models import Pet


class HomeView(ListView):
    '''Render home page'''

    def get(self, req):
        return render(req, 'home.html')


class PetCreateView(CreateView):
    model = Pet
    fields = ['pet_name', 'species', 'breed', 'weight_in_pounds', 'owner']
    template_name = 'create_pet.html'


class PetsView(ListView):
    model = Pet

    def get(self, req):
        pets = self.get_queryset().all()
        return render(req, 'pets.html', {
            'pets': pets
        })
