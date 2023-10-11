from . import views
from django.urls import path

app_name = 'ristoranApi'
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant/statistics/', views.RestaurantSpatialViews.as_view(), name='restaurant_by_location'),
    path('restaurant/<str:id>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]
