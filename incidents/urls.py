from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_incidents, name="category"),
    path("incident/<slug:slug>/", views.incident_detail, name="incident_detail"),
    path("<slug:slug>/", views.incident_detail, name="incident_detail"),

]
