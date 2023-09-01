from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="index"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('tracker/', views.tracker, name="tracker"),
    path('donate/', views.donate, name="donate"),
    path('work/', views.work, name="work"),
]
