from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
