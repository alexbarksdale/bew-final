from . import views
from django.urls import path
from pets.views import HomeView, PetCreateView, PetsView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('create/', PetCreateView.as_view(), name='pet-create-page'),
    path('pets/', PetsView.as_view(), name='pets-page')
]
