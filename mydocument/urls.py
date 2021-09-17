from django.urls import path

from . import views

urlpatterns = [

    path('', views.userdocument, name='userdocument'),

]