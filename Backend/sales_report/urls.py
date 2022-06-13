# create urls
from django.urls import path
from . import views
#


urlpatterns = [
    path('saleReport/', views.index.as_view(), name='index'),
]