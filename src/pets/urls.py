from . import views
from django.urls import path
from pets.views import HomeView, PetCreateView, PetsListView, PetDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('pets/', PetsListView.as_view(), name='pets-list-page'),
    path('create/', PetCreateView.as_view(), name='pet-create-page'),
    path('pets/<int:pet_id>/', PetDetailView.as_view(), name='pet-detail-page'),

]
