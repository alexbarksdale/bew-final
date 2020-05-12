from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from pets.models import Pet, Appointment


class PetTests(TestCase):
    def test_list_page(self):
        # Instance of user to test the pages
        user = User.objects.create_user(username='test', password='testing123')
        self.client.login(username='test', password='testing123')

        # Create a test pet
        pet = Pet.objects.create(pet_name='Ricky',
                                 species='Dog',
                                 breed='Husky',
                                 weight_in_pounds=55.6,
                                 owner=user)
        pet.save()  # save our pet

        # Making a GET request to check if the pet is in the results (list page)
        res = self.client.get(f'/pets/')

        # Very a 200 response
        self.assertEqual(res.status_code, 200)

        # Check if the page contains a pet with the name Ricky
        self.assertContains(res, 'Ricky')

        # Get pet object to check if the user's pet exists
        pet_object = Pet.objects.get(owner=user)
        self.assertEqual(pet_object.owner, user)

    def test_detail_page(self):
        # Instance of user to test the pages
        user = User.objects.create_user(username='test', password='testing123')
        self.client.login(username='test', password='testing123')

        # Create a test pet
        pet = Pet.objects.create(pet_name='Ricky',
                                 species='Dog',
                                 breed='Husky',
                                 weight_in_pounds=55.6,
                                 owner=user)
        pet.save()  # save our pet

        # Create an appointment
        appointment = Appointment.objects.create(date_of_appointment=timezone.now(),
                                                 duration_minutes=30,
                                                 special_instructions='Leave door open',
                                                 pet=pet)
        appointment.save()  # save appointment

        # Making a GET request to check if the pet is in the results (detail page)
        res = self.client.get(f'/pets/{pet.id}/')
        # Very a 200 response
        self.assertEqual(res.status_code, 200)

        # Get pet object to check
        pet_object = Pet.objects.get(pet_name='Ricky')
        # Check if the pet's name appears in the result
        self.assertEqual(pet_object.pet_name, 'Ricky')

    def test_pet_create_page(self):
        # Instance of user to test the pages
        user = User.objects.create()

        post_data = {
            'pet_name': 'Ricky',
            'species': 'Dog',
            'breed': 'Husky',
            'weight_in_pounds': 55.6,
            'owner': user.id
        }

        # Request to create a post
        res = self.client.post('/pet/create/', data=post_data)

        # Very a 302 response
        self.assertEqual(res.status_code, 302)

        # Get pet object to check
        pet_object = Pet.objects.get(pet_name='Ricky')

        # Check if the pet was creaetd
        self.assertEqual(pet_object.pet_name, 'Ricky')

    def test_create_appointment_page(self):
        '''Cannot figure out why the appointment isn't retrieving the test 
        post_data. I spoke with you on zoom about it, but we weren't able to figure it out.
        However, the site is fully functional and I demoed the appointment to you.'''
        # Instance of user to test the pages
        user = User.objects.create()

        # Create a test pet
        pet = Pet.objects.create(pet_name='Ricky',
                                 species='Dog',
                                 breed='Husky',
                                 weight_in_pounds=55.6,
                                 owner=user)
        pet.save()

        post_data = {
            'date_of_appointment': '2020-2-2',
            'duration_minutes': 30,
            'special_instructions': 'Leave door open',
            'pet': pet
        }

        # Request to create an appointment
        res = self.client.post('/appointment/create/', data=post_data)

        self.assertEqual(res.status_code, 200)

        # ===== Uncommenting the content in here works, but the post request works. Super strange =====
        # appointment = Appointment.objects.create(date_of_appointment='2020-2-2',
        #                                          duration_minutes=30,
        #                                          special_instructions='Leave door open',
        #                                          pet=pet)
        # appointment.save()  # save appointment
        # =============================================================================================

        app_object = Appointment.objects.get(date_of_appointment='2020-2-2')

        self.assertEqual(app_object.date_of_appointment,
                         datetime.date(2020, 2, 2))
