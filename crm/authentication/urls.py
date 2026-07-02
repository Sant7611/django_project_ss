from django.urls import path
from . import views

urlpatterns = [
    path('plaintext/', views.plain_text, name='plain_text'),
    path('Student/', views.json_text, name='plain_text'),
    path('image_return/', views.image_return, name='image_return'),
    path('html_render/', views.html_render, name='html_render')
]
