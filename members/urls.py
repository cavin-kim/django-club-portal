from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.member_list, name="member_list"),
]
