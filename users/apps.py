from django.apps import AppConfig


# This file specifies one of the Django apps we decided to base our application on. We chose to use the "profile"
# application after having generated and reviewed all the user journeys we initially came up with. These
# user journeys can be accessed in our report.


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
    	import users.signals
