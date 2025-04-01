from .views import main, about, services, contact
from django.urls import path, include

urlpatterns = [
    path("", main, name="main"),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),

]
