"""IpekProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from products import views
from django.contrib import admin
from django.urls import path, include

from products.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
    path('', views.product_list.as_view() , name=product_list) 
    
]
