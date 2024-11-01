from django.test import TestCase
from ..models import Player

# Create your tests here.
class PlayerModelTest(TestCase):
    def test_player_creation(self):
        player = Player.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='2000-01-01',
            email='johndoe@example.com',
            phone_number='123-456-7890'
        )

        self.assertEqual(player.first_name, 'John')
        self.assertEqual(player.last_name, 'Doe')
        self.assertEqual(player.email, 'johndoe@example.com')
        self.assertEqual(player.phone_number, '123-456-7890')