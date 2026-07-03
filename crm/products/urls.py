from django.urls import path
from . import views

urlpatterns = [
    path('serializer/', views.show_serializers, name='show_serializer'),
]