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
    url(r'^admin/', admin.site.urls),  # admin portal
    url(r'^start/$', starter),  # brains of the design
    url(r'^time/$', current_datetime),  # simple and learning experince
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),  # simple and learning experince
    url(r'^members/$', users, name='users'),  # View of current members under Blogger(model)
    url(r'^news/$', entry, name='news'),  # Post entry view [ entire Entry(model) ]
    url(r'^post/new/$', post_new, name='post_new'),  # create new post if logged_in
    url(r'^base/$', base),
    url(r'^contact/$', contact),  # simple form with contact abilities ref. email
    url(r'^contactpopup/$', contact_popup),  # (in development) test run for [contact us] to be inside a " bootstrap modal "
    url(r'^$', home),  # home
    url(r'^login/$', 'django.contrib.auth.views.login'),  # django login
    url(r'^logout/$', 'django.contrib.auth.views.logout'),  # django logout
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),  # Post edit ( view and edit just one post [ post/<1 2 3 4>/ ] )
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),  # Post in-view ( view just one post post/<1 2 3 4>/ Than gives you the choice to edit if logged_in )
    url(r'^polls/', include('tuts.urls')),  # tut app ( Tutorials ) URL Include
    url(r'^polls/', include('FirstApp.urls')),  # tut app ( Tutorials ) URL Include

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
