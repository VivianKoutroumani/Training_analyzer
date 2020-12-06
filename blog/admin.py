from django.contrib import admin
from .models import Workout


# This file delineates which tables and the data contained therein should be accessible from the "admin" section of the
# website. From the admin page, one can update the information associated with any workout, delete any workout, and
# add a workout.


admin.site.register(Workout)
