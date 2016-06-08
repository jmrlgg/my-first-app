from . import views
from django.conf.urls import *
from django.contrib import admin
from FirstApp.views import *
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),  # admin portal
]
