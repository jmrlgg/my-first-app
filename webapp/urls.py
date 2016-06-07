"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# views shortcut - instead of (from FirstApp.views import foo, current_time, news, blog) = ( from FirstApp.views import *)
from django.conf.urls import *
from django.contrib import admin
from FirstApp.views import *
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^start/$', starter),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^members/$', users, name='users'),
    url(r'^news/$', entry, name='news'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^base/$', base),
    url(r'^contact/$', contact),
    url(r'^contactpopup/$', contact_popup),
    url(r'^$', home),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]

# urlpatterns = patterns('FirstApp.views',
#     (r'^admin/', admin.site.urls),
#     (r'^start/$', starter),
# 	(r'^time/$', current_datetime),
# 	(r'^time/plus/(\d{1,2})/$', hours_ahead),
# 	(r'^post/$', news),
# 	(r'^base/$', base),
# 	(r'^contact/$', contact),
# 	(r'^$', home),
# )
