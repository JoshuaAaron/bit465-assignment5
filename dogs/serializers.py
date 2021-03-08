#dogapi/serializers.py

from rest_framework import serializers
from dogs.models import Dog
from dogs.models import Breed
import dogs.controllers

class DogSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    # We want to display the dog breeds name instead of the id 
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dog
        fields = ('id',
                  'name',
                  'age',
                  'breed',
                  'gender',
                  'color',
                  'favoriteFood',
                  'favoriteToy' )

# Breed
class BreedSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    name = serializers.CharField()
    dogs = DogSerializer(many=True, read_only=True) 
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Breed
        fields = ('id',
                  'name',
                  'size',
                  'friendliness',
                  'trainability',
                  'sheddingamount',
                  'exerciseneeds',
                  'dogs')

