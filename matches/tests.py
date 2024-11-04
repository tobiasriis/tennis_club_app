from django.test import TestCase

from django.test import TestCase
from .models import Match

from courts.models import Court
from users.models import Player
from datetime import date


class MatchTestCase(TestCase):
    def setUp(self):
        self.court = Court.objects.create()

        self.player_1 = Player.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 1, 1),
            phone_number="1234567890",
            email="john.doe@example.com",
        )

        self.player_2 = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            date_of_birth=date(1992, 5, 15),
            phone_number="0987654321",
            email="jane.smith@example.com",
        )
        self.match = Match.objects.create(
            court_id=self.court.id,
            player_1=self.player_1,
            player_2=self.player_2,
        )

    def test_point_won_before_advantage(self):
        self.match.player_1_point_score = 40
        self.match.player_2_point_score = 15

        self.match.add_point_player_1()

        self.assertEqual(self.match.player_1_game_score, 1)
        self.assertEqual(self.match.player_1_point_score, 0)
        self.assertEqual(self.match.player_2_point_score, 0)

    def test_deuce_to_advantage(self):
        self.match.player_1_point_score = 40
        self.match.player_2_point_score = 40

        self.match.add_point_player_1()

        self.assertEqual(self.match.player_1_point_score, 2)
        self.assertEqual(self.match.player_2_point_score, 1)

    def test_advantage_to_game_won(self):
        self.match.player_1_point_score = 2
        self.match.player_2_point_score = 1

        self.match.add_point_player_1()

        self.assertEqual(self.match.player_1_game_score, 1)
        self.assertEqual(self.match.player_1_point_score, 0)
        self.assertEqual(self.match.player_2_point_score, 0)

    def test_normal_point_increment(self):
        self.match.player_1_point_score = 0
        self.match.player_2_point_score = 15

        self.match.add_point_player_1()

        self.assertEqual(self.match.player_1_point_score, 15)
        self.assertEqual(self.match.player_2_point_score, 15)
