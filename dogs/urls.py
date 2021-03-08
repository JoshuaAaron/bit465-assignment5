# dogs/urls.py

from django.conf.urls import url

from . import controllers

urlpatterns = [
    url(r'^dogs/$',  
        controllers.DogList.as_view(), 
        name=controllers.DogList.name), 
    url(r'^dogs/(?P<pk>[0-9]+)/$',  
        controllers.DogDetails.as_view(), 
        name=controllers.DogDetails.name), 
    url(r'^breeds/$',  
        controllers.BreedList.as_view(), 
        name=controllers.BreedList.name), 
    url(r'^breeds/(?P<pk>[0-9]+)/$',  
        controllers.BreedDetails.as_view(), 
        name=controllers.BreedDetails.name),
    url(r'^$', 
        controllers.ApiRoot.as_view(), 
        name=controllers.ApiRoot.name),

]
