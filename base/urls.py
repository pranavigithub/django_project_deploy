from django.urls import path

from. import views

urlpatterns=[
    path("404/", views.handler404, name="404"),
    path("500/", views.handler500, name="500"),
    path("main/", views.base, name="base"),
]