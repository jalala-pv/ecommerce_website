
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('products_list', views.list_products,name='list_product'),


]