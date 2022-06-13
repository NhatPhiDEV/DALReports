'''
    create_urls.py
'''
from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.index.as_view(), name='index'),
]