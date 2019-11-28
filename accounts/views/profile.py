from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class CreateProfile(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "accounts/profile_create.html")

    def post(self, request):
        pass