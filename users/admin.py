from django.contrib import admin
from .models import Profile


# This file delineates which tables and the data contained therein should be accessible from the "admin" section of the
# website. From the admin page, one can update the information associated with any profile. One must specify this
# functionality for the "Profile" table since it is not stored within the "blog" application.


admin.site.register(Profile)
