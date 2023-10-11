# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.views import View
from django.contrib.gis.geos import Point
from . import models

restaurant_msgs: dict = {
    "not_found": "restaurant not found",
    "deleted": "restaurant deleted successfully",
    "updated": "restaurant updated",
    "created": "restaurant created",
    "error": "an error has ocurred"
}
def index(_):
    return JsonResponse({"message":"Hello, world. You're at the index."},)

class RestaurantListView(View):
    def get(self, request):
        queryset = models.Restaurant.objects.all()
        restaurants = []
        for restaurant in queryset:
            restaurants.append({
                'id': restaurant._id,
                'name': restaurant.name,
                'street': restaurant.street,
                'phone': restaurant.phone,
                'email': restaurant.email,
                'lat': restaurant.location.x,
                'lng': restaurant.location.y,
            })
        return JsonResponse(restaurants, safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        try:
            restaurant = models.Restaurant.objects.create(
                _id = data['id'],
                rating = data['rating'],
                name = data['name'],
                site = data['site'],
                email = data['email'],
                phone = data['phone'],
                street = data['street'],
                city = data['city'],
                state = data['state'],
                location = Point(float(data['lat']), 
                                 float(data['lng'])),
            )
            return JsonResponse({
                'id': restaurant._id,
                'name': restaurant.name,
                'street': restaurant.street,
                'city': restaurant.city,
                'phone': restaurant.phone,
                'email': restaurant.email,
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class RestaurantDetailView(View):
    def get(self,_,id):
        if id is None:
            return JsonResponse({'error': 'id is required'}, status=400)
        try:
            res_found = models.Restaurant.objects.get(_id=id)
            response = res_found.get_dict()
            return JsonResponse(response, status=200, safe=False)
        except models.Restaurant.DoesNotExist:
            return JsonResponse({'error': restaurant_msgs['not_found']}, status=404)
    
    def put(self, request, id):
        data = json.loads(request.body)
        try:
            res_found = models.Restaurant.objects.get(_id=id)
            for key,value in data.items():
                if key not in models.Restaurant.__dict__.keys():
                    continue
                if key == '_id':
                    continue
                setattr(res_found, key, value)
            res_found.save()
            return JsonResponse({'message': restaurant_msgs['updated'], 
                                 "object":{**res_found.get_dict()}}, status=200)
        except models.Restaurant.DoesNotExist:
            return JsonResponse({'error': restaurant_msgs['not_found']}, status=404)

    def delete(self, _, id):
        if id is None:
            return JsonResponse({'error': 'id is required'}, status=400)
        try:
            res_found = models.Restaurant.objects.get(_id=id)
            res_found.delete()
            return JsonResponse({'message': restaurant_msgs['deleted']}, status=200)
        except models.Restaurant.DoesNotExist:
            return JsonResponse({'error': restaurant_msgs['not_found']}, status=404)

class RestaurantSpatialViews(View):
    def get(self,request):
        lat = request.GET.get('lat', None)
        lng = request.GET.get('lng', None)
        radius = request.GET.get('radius', None)
        try:
            lat = float(lat)
            lng = float(lng)
            radius = float(radius)
        except ValueError:
            return JsonResponse({'error': 'lat, lng and radius must be float'}, status=400)
        try:
            new_point = Point(lat, lng)
            print(new_point)
            queryset = models.Restaurant.objects.filter(
                location__distance_lte=(new_point, radius)
            )
            restaurants = []
            for restaurant in queryset:
                restaurants.append({
                    'id': restaurant._id,
                    'name': restaurant.name,
                    'street': restaurant.street,
                    'phone': restaurant.phone,
                    'email': restaurant.email,
                })
            return JsonResponse(restaurants, safe=False)
        except models.Restaurant.DoesNotExist:
            return JsonResponse({'error': 'ERROR PAPU'}, status=404)