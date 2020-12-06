from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# When users enter information on FitHub, their information is stored in a table called "Workout." The class below
# called "Workout" inherits the Model class from Django and specifies all the attributes which belong to the "Workout"
# entity. The comments below explain which attributes of the table are created by a given section of code.


class Workout(models.Model):

    # The attributes created by the following three lines of code are quite straightforward. It's worth understanding
    # that even though "timezone.now" is a function, it is not executed because it is not followed by parentheses.
    # What this code does is set the default time displayed in each of the fields to the time at which the user is
    # entering their workout data. What's more is that it allows them to update the date and time fields after having
    # entered the data originally. In addition, these fields are only updated when the user wants to update them.
    date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    # These two lines create the attributes which allow the user to describe their workout with a title and a bit of
    # description. If the user decides to not specify either of these attributes when entering a workout, these cells
    # will display three asterisks instead.
    title = models.CharField(max_length=75)
    description = models.TextField()

    # This class creates a set of choices to which the "sport" field refers. Essentially what it is doing is creating a
    # drop-down menu of options from which the user can choose when entering their workout data. The first quoted value
    # is the information which is stored in the "Workout" table, while the second quoted value is what is displayed to
    # the user when they are entering a workout.
    class SportChoices(models.TextChoices):
        CYCLING = 'Cycling', _('Cycling')
        HIKING = 'Hiking', _('Hiking')
        LIFTING = 'Lifting Weights', _('Lifting Weights')
        RUNNING = 'Running', _('Running')
        SWIMMING = 'Swimming', _('Swimming')
        WALKING = 'Walking', _('Walking')
        YOGA = 'Yoga', _('Yoga')

    # This field stores the type of sport in which the user engaged. It references the "Sport Choices" class we just
    # discussed. Furthermore, it specifies a default option as well as that this field cannot be null.
    sport = models.CharField(
        max_length=15,
        choices=SportChoices.choices,
        default=SportChoices.RUNNING,
        blank=False
    )

    # This class creates a set of choices to which the "type" field refers. Like the "Sport Choices" class, it is
    # essentially creating a drop-down menu of options from which the user can choose when entering their workout data.
    # The first quoted value is the information which is stored in the "Workout" table, while the second quoted value
    # is what is displayed to the user when they are entering a workout.
    class TypeChoices(models.TextChoices):
        DISTANCE = 'Distance', _('Distance')
        INTERVAL = 'Interval', _('Interval')
        NONE = 'None', _('None')
        RACE = 'Race', _('Race')
        STRESS = 'Stress Relief', _('Stress Relief')
        TYPE_WORKOUT = 'Workout', _('Workout')

    # This field stores the type of workout in which the user engaged. It references the "Type Choices" class we just
    # discussed. Furthermore, it specifies a default option as well as that this field cannot be null.
    type = models.CharField(
        max_length=15,
        choices=TypeChoices.choices,
        default=TypeChoices.NONE,
        blank=False
    )

    # This field allows the user to record how much distance they covered during their workout. The specifications we
    # chose allow users to enter workouts which cover at most 999.99 kilometers. We figured this was a reasonable
    # upper-bound.
    distance = models.DecimalField(max_digits=5, decimal_places=2)

    # This class creates a set of choices to which the "intensity" field refers. It is specified in a similar way to
    # that of "Sport Choices" and "Type Choices."
    class MetChoices(models.TextChoices):
        EASY = 'Easy', _('Easy')
        MODERATE = 'Medium', _('Moderate')
        HARD = 'Hard', _('Hard')

    # This field stores the intensity of the workout in which the user engaged. It references the "Met Choices"
    # class we just discussed. Furthermore, it specifies a default option as well as that this field cannot be null.
    workout_intensity = models.CharField(
        max_length=10,
        choices=MetChoices.choices,
        default=MetChoices.MODERATE,
        blank=False
    )

    # This field stores the username of the user which is logged into FitHub at the time of workout entry. It is a
    # foreign key to the "User" table, which is specified in the "users.model.py" folder. Note that when a user is
    # deleted from the site, all of the workouts they entered are deleted, too.
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)

    # This method allows us to calculate how long a particular workout lasts.
    def activity_duration(self):
        duration = datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.start_time)
        return duration

    def get_absolute_url(self):
        return reverse('workout-detail', kwargs={'pk': self.pk})

    # This method is quite specific! It makes it so that if one is querying the data stored in the "Workout" table from
    # a Python shell in the terminal, only the title of the applicable workout(s) is/are returned in the query set. This
    # makes the results shown in the query set much more useful to the person who is querying the data.
    def __str__(self):
        return self.title


# This class created a model called "Posts." This model was used as a test case for us to experience the Django
# platform and understand how it works. We did not delete this code, however, due to dependency concerns.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_time = models.IntegerField(default=0)
    workout_distance = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('workout-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
