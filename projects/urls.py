# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    # root url connects to project_index
    path("", views.project_index, name="project_index"),
    # url endpoint must be /1 or /2 or whatever the project primary key is
    path("<int:pk>/", views.project_detail, name="project_detail"),
]