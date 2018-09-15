from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]