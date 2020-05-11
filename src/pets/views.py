from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from pets.models import Pet, Appointment


class HomeView(ListView):
    '''Render home page'''

    def get(self, req):
        return render(req, 'home.html')


class PetCreateView(CreateView):
    '''Create a pet form'''
    model = Pet
    fields = ['pet_name', 'species', 'breed', 'weight_in_pounds']
    template_name = 'pet/create_pet.html'


class PetsListView(ListView):
    '''Render created pets'''
    model = Pet

    def get(self, req):
        pets = self.get_queryset().all()
        return render(req, 'pet/pet_list.html', {
            'pets': pets
        })


class PetDetailView(DetailView):
    '''Render pet information'''

    def get(self, req, pet_id):
        return render(req, 'pet/pet_detail.html', {
            'pet': Pet.objects.get(id=pet_id)
        })


class AppointmentCreateView(CreateView):
    '''Create an appointment form'''
    model = Appointment
    fields = ['date_of_appointment',
              'duration_minutes', 'special_instructions', 'pet']
    template_name = 'calender/create_appointment.html'


class CalenderListView(ListView):
    '''Render all appointments'''
    model = Appointment

    def get(self, req):
        appointments = self.get_queryset().all()
        return render(req, 'calender/calender_list.html', {
            'appointments': appointments.filter(
                # renders things greater than today's date
                date_of_appointment__gte=timezone.now()
                # Sorts by the soonest first. Put '-' in front of the first argument for greatest to least.
                # Example: '-date_of_appointment' === greatest to least order
            ).order_by('date_of_appointment', 'date_of_appointment')
        })
