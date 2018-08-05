"""taskmanager_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from taskapp.views import add as view_add
from taskapp.views import home as view_home
from taskapp.views import about, sign_up, cong, sign_in, sign_out, task_detail, before, compled

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', view_add, name='add'),
    path('', view_home, name='home'),
    path('sign_up/', sign_up, name='sign_up'),
    path('cong/', cong, name='cong'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path('task/<int:pk>/', task_detail, name='task_detale'),
    path('old/', before, name='before'),
    path('compled/', compled, name='compled'),
    path('about/', about, name='about'),
]
