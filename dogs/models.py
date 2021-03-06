from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Breed Model
class Breed(models.Model):
    TINY = 'tiny'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    BREED_SIZE_CHOICES = [
        (TINY, 'tiny'),
        (SMALL, 'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large'),
    ]
    size = models.CharField(
        max_length=6,
        choices=BREED_SIZE_CHOICES,
        default=TINY,
    )

    name = models.CharField(max_length=50, blank=False)
    # (a character string) [should accept Tiny, Small, Medium, Large]
    friendliness = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    trainability = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    sheddingamount = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    exerciseneeds = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name) 

# Dog model
class Dog(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=30, blank=False)
    favoriteFood = models.CharField(max_length=50, blank=False)
    favoriteToy = models.CharField(max_length=50, blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name) 