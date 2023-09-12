from django.urls import path
from . import views

urlpatterns = [
    path('',view.RegisterView.as_view(),name='register_page')
]