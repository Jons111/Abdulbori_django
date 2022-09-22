"""djangofiles URL Configuration

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
from django.contrib import admin
from django.urls import path
from myfiles.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='soz'),
    path('Oqituvchilar/', salom, name='soz1'),
    path('Oquvchilar/', salom1, name='soz2'),
    path('add_s/',talaba_qoshish,name='adding1'),
    path('del1/<sss>/',delete_student,name='del_student'),
    path('update_t/<id>/',update_teacher,name = 'update_teach')

]
