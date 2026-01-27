from django.urls import path
from home.views import hello_world

urlpatterns = [
    path('credit/', hello_world),
]