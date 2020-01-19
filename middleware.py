import logging
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from re import compile
from django.urls import resolve
from django.shortcuts import redirect

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(object):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).
    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        """Let's handle old-style request processing here, as usual."""
        # Do something with request
        # Probably return None
        # Or return an HttpResponse in some cases


        return None

    def process_response(self, request, response):
        """Let's handle old-style response processing here, as usual."""
        # Do something with response, possibly using request.
        print('******* LoginRequiredMiddleware *********')
        return response

    def __call__(self, request):

        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE setting to insert\
 'django.contrib.auth.middleware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."

        path = request.path_info.lstrip('/')
        url_name = resolve(request.path_info).url_name

        print('******* LoginRequiredMiddleware 1 *********')

        # if not request.user.is_authenticated:
        #     if not any(m.match(path) for m in EXEMPT_URLS):
        #         return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)


class SetGroupMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        path = request.path_info.lstrip('/')

        # if path != 'admin/' and not request.user.employee.is_password_change:
        #     print(path)
        #     print('*****************************************')
        #     print('change password')
        #     print('*****************************************')

        # return HttpResponseRedirect('change_password/')

        if not any(m.match(path) for m in EXEMPT_URLS):
            print('******* SetGroupMiddleware *********')

            try:
                request.branch = request.user.employee.branch
                request.groups = list(request.user.groups.values_list('name', flat=True))
            except Exception as e:
                # this is for django-admin, as that user may not belong to bank users
                request.branch = None
                request.groups = []

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
