"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]

from django.urls import include, path
from django.contrib import admin
from .api import router

from rental import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/',myapp_views.UserLoginApiView.as_view()),
    path('api/v1/', include(router.urls)),
    # path(r'api/v1/auth/', include('rest_auth.urls')),)
]
