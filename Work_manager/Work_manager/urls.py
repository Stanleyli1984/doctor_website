"""Work_manager URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
#from TasksManager import views
from TasksManager.new_doctor_information import views as new_doctor_view
from TasksManager.new_doctor_information import process_name as new_doctor_process_name
from TasksManager.pictures import views as pictures_view

urlpatterns = [
    url (r'^admin/', admin.site.urls),
    url (r'^process_name/', new_doctor_process_name.process),
    url (r'^$', new_doctor_view.add_doctor),
    url (r'^display$', new_doctor_view.display_doctors),
    url (r'^uploadpics$', pictures_view.upload_pictures),
    #url (r'^index$', views.index.page),
]
