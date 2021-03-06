"""ark_service URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from arkapp import views as arkapp_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', arkapp_views.homepage, name='homepage'),
    url(r'^mint/$', arkapp_views.mint, name='mint'),
    url(r'^bind/$', arkapp_views.bind, name='bind'),
    url(r'^resolve/$', arkapp_views.resolve, name='resolve'),
]
