from django.urls import path
from .import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path("data/", views.html_render, name="html_data"),
    path("class_html/", views.HomePageView.as_view(), name="class-temp-html-data"),

    # Forms
    path("fun_wodf/", views.from_user, name="fun-wodj"),
    path("fun_wdf/", views.from_user_django_form, name="fun-wdj")
]