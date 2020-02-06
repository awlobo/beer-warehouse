from django.core.exceptions import PermissionDenied


def simple_middleware(get_response):
   def middleware(request):
       if not request.user.is_superuser:
           raise PermissionDenied
       response = get_response(request)
       return response
   return middleware
