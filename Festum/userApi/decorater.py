from django.http.response import JsonResponse

def allowuser(allowrole = []):
    def decorators(new_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.user_type in allowrole:
                return new_func(request, *args, **kwargs)
            else :
                return JsonResponse({
                    "message" : "user is not allowed to access",
                    "data" : 0,
                    "isSuccess" : False
                    }, status=403)
        return wrapper_func
    return decorators
