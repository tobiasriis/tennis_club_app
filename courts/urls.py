from django.urls import path
from . import views

app_name = "courts"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:court_id>", views.court_detail, name="court_detail"),
    path("add/", views.court_add, name="court_add"),
    path("edit/<int:court_id>/", views.court_edit, name="court_edit"),
    path("delete/<int:court_id>/", views.court_delete, name="court_delete"),
    path("reservations/", views.reservation_list, name="reservation_list"),
    path("reservations/new/", views.reservation_add, name="court_reservation_add"),
]
