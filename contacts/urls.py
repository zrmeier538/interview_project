from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^admin/', admin.site.urls),
]