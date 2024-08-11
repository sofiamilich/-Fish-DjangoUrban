"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from example1.views import index,third_task, index1
from task4.views import index, third_task, index1, menu
# from task4.views import views
from django.views.generic import TemplateView
from task5.views import sign_up_by_django, sign_up_by_html
from task2.views import function_template, class_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', third_task),
    path('index/', index),
    # path('index/', include('UrbanDjango.urls')),
    path('index1/', index1),
    # path('index/index1/', index1, name='index1'),
    path('menu/', menu),
    path('sign_up_by_django/', sign_up_by_django),
    path('sign_up_by_html/', sign_up_by_html),
    path('function_template/', function_template),
    path('class_template/', class_template.as_view()),
]
