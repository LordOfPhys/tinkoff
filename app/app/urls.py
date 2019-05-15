from django.conf.urls import url
from django.contrib import admin
from TINKOFF import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^index/$', views.index, name = 'index'),
        url(r'^login/$', views.log, name = 'login'),
        url(r'^logout/$', views.logout_view, name = 'logout'),
        url(r'^admin/', admin.site.urls),
 ]
