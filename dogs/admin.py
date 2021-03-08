from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Dog
from .models import Breed

admin.site.register(Dog)
admin.site.register(Breed)