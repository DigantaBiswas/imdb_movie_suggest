from django.urls import re_path as url, path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path("", views.home, name='home_url'),
    path("", views.suggestion, name='suggestion_url')

]
