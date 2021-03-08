# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from dogs.serializers import DogSerializer
from dogs.serializers import BreedSerializer
from dogs.models import Dog
from dogs.models import Breed
# Create your views here.
#dogs/controllers.py

#root class
class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'dogs': reverse(DogList.name, request=request), 
            'breeds': reverse(BreedList.name, request=request),  
            })

#dogs
class DogList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name="create"
    def perform_create(self, serializer):
        """Save the post data when creating a new dog."""
        serializer.save()

class DogDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name="details"
    
#breeds
class BreedList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name="breed-create"
    def perform_create(self, serializer):
        """Save the post data when creating a new Breed."""
        serializer.save()

class BreedDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name="breed-details"
