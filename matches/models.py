from django.db import models
from datetime import datetime, time, timedelta


class Match(models.Model):
    class Status(models.TextChoices):
        PENDING = "P", "Pending"
        ONGOING = "O", "Ongoing"
        FINISHED = "F", "Finished"

    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.PENDING,
    )

    # match details
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    player_1 = models.ForeignKey(
        "users.Player", on_delete=models.PROTECT, related_name="player_1_matches"
    )
    player_2 = models.ForeignKey(
        "users.Player", on_delete=models.PROTECT, related_name="player_2_matches"
    )
    court = models.ForeignKey("courts.court", on_delete=models.PROTECT)

    # control vars
    set_number = models.IntegerField(default=1)

    # score variables
    player_1_set_score = models.IntegerField(default=0)
    player_2_set_score = models.IntegerField(default=0)
    player_1_game_score = models.IntegerField(default=0)
    player_2_game_score = models.IntegerField(default=0)
    player_1_point_score = models.IntegerField(default=0)
    player_2_point_score = models.IntegerField(default=0)

    final_scores = models.JSONField(
        default=dict
    )  # e.g., {"sets": [{"player1": 6, "player2": 4}]}

    point_score_table = {
        0: 15,
        15: 30,
        30: 40,
        40: {"advantage": 2, "deuce": 1},
    }

    def set_won(self, player):
        current_score = dict(self.final_scores)
        current_score[str(self.set_number)] = {
            "player_1_score": self.player_1_game_score,
            "playe_r2_score": self.player_1_game_score,
        }
        self.final_scores = current_score
        self.set_number += 1

    def game_won(self, player):
        # reset point scores
        self.player_1_point_score = 0
        self.player_2_point_score = 0

        # increase game score

    def add_point_player_1(self):

        # point is won by player 1 from advantage
        if self.player_1_point_score == self.point_score_table[40]["advantage"]:
            self.player_1_game_score += 1
            self.player_1_point_score = 0
            self.player_2_point_score = 0
            self.game_won(self.player_1)

        # deuce
        elif (
            self.player_1_point_score == self.point_score_table[40]["deuce"]
            or self.player_1_point_score == 40
            and self.player_2_point_score == 40
        ):
            self.player_1_point_score = self.point_score_table[40]["advantage"]
            self.player_2_point_score = self.point_score_table[40]["deuce"]

        # point is won by player 1 before advantage
        elif self.player_1_point_score == 40 and self.player_2_point_score <= 30:
            self.player_1_game_score += 1
            self.game_won(self.player_1)

        else:
            self.player_1_point_score = self.point_score_table[
                self.player_1_point_score
            ]
