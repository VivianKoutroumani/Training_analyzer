from django.contrib import admin
from .models import Post, Country, City, Workout

admin.site.register(Post)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Workout)