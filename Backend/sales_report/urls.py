# create urls
from django.urls import path
from . import views
#


urlpatterns = [
    path('saleReport/', views.index.as_view(), name='index'),
    path('saleReport/column_name_list/', views.column_name_list.as_view(), name='column_name_list'),
]