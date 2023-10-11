from . import views
from django.urls import path

app_name = 'ristoranApi'
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant/<str:id>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]
