from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('<slug:slug>', views.product_detail, name='product-detail')
]