from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


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


class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()


class Workout(models.Model):
    date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=75)
    description = models.TextField()

    class SportChoices(models.TextChoices):
        CYCLING = 'Cycling', _('Cycling')
        HIKING = 'Hiking', _('Hiking')
        LIFTING = 'Lifting Weights', _('Lifting Weights')
        RUNNING = 'Running', _('Running')
        SWIMMING = 'Swimming', _('Swimming')
        WALKING = 'Walking', _('Walking')
        YOGA = 'Yoga', _('Yoga')

    sport = models.CharField(
        max_length=15,
        choices=SportChoices.choices,
        default=SportChoices.RUNNING,
        blank=False
    )

    class TypeChoices(models.TextChoices):
        DISTANCE = 'Distance', _('Distance')
        INTERVAL = 'Interval', _('Interval')
        NONE = 'None', _('None')
        RACE = 'Race', _('Race')
        STRESS = 'Stress Relief', _('Stress Relief')
        TYPE_WORKOUT = 'Workout', _('Workout')

    type = models.CharField(
        max_length=15,
        choices=TypeChoices.choices,
        default=TypeChoices.NONE,
        blank=False
    )

    distance = models.DecimalField(max_digits=5, decimal_places=2)

    class MetChoices(models.TextChoices):
        EASY = 'Easy', _('Easy')
        MODERATE = 'Medium', _('Moderate')
        HARD = 'Hard', _('Hard')

    workout_intensity = models.CharField(
        max_length=10,
        choices=MetChoices.choices,
        default=MetChoices.MODERATE,
        blank=False
    )

    athlete = models.ForeignKey(User, on_delete=models.CASCADE)

    def activity_duration(self):
        duration = datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.start_time)
        return duration

    def get_absolute_url(self):
        return reverse('workout-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
