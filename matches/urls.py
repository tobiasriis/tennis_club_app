from django.urls import path
from . import views

app_name = "matches"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:court_id>", views.match_detail, name="match_detail"),
    path("add/", views.match_add, name="match_add"),
    path("edit/<int:court_id>/", views.match_edit, name="match_edit"),
    path("delete/<int:court_id>/", views.match_delete, name="match_delete"),
]
