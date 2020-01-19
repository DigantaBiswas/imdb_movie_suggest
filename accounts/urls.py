from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from .views.profile import CreateProfile

app_name = 'accounts'
urlpatterns = [
	path("create-profile/", CreateProfile.as_view(), name="create_profile"),

]