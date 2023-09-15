from django.urls import path, include
from api import views

urlpatterns = [
    path('test/', views.test, name='test'),
]