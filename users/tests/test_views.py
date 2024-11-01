from django.test import TestCase
from django.test import Client
from ..models import Player
from ..views import index

class IndexViewTest(TestCase):
    def setUp(self):
        # BUILD
        Player.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1990-01-01',
            email='johndoe@example.com'
        )
        Player.objects.create(
            first_name='Jane',
            last_name='Smith',
            date_of_birth='1995-07-15',
            email='janesmith@example.com'
        )

    def test_index(self):
        client = Client()
        response = client.get('/users/')
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        # Check template rendering
        self.assertTemplateUsed(response, 'users/index.html')
        # Check context data
        players = response.context['players']
        self.assertEqual(len(players), 2)