from . import views
from django.urls import path

app_name = 'ristoranApi'

urlpatterns = [
    path('', views.index, name='index'),
]