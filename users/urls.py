from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:player_id>", views.player_detail, name="player_detail"),
    path("add/", views.add_user, name="add_user"),
    path("player/edit/<int:player_id>/", views.edit_player, name="edit_player"),
    path("player/delete/<int:player_id>/", views.delete_player, name="delete_player"),
]
