from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            return self.get_response(request)

        current_route_name = resolve(request.path_info).url_name

        exempt_urls = ['login']

        if current_route_name not in exempt_urls:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
