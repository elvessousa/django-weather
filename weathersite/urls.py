from django.urls import path
from weathersite import views

urlpatterns = [
    path('', views.index, name='index')
]
