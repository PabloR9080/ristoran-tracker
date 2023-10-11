from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if '/api/v1/' not in request.path or '/api/v1/restaurant/' in request.path: 
            response = self.get_response(request)
            return response
        
        jwt_authenticator = JWTAuthentication()
        try:
            user, _ = jwt_authenticator.authenticate(request)

            if user is not None:
                request.user = user
            else:
                return JsonResponse({"message":"Access denied. Invalid or missing token."}, status=403)
            response = self.get_response(request)
            return response
        except Exception as e:
            return JsonResponse({"message":"Access denied. Invalid or missing token."}, status=403)
