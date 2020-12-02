from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


"""
This migration creates the "Workout" table, which was critical to the implementation of our workout analysis
application. The addition of this table to the application allows users to record all their historical workouts in one
place. Its addition also permits the application to conduct analyses on their historical information. See the comments
below for a line-by-line explanation as to what this migration does. It's worth highlighting that this file does not
get run until the user specifically calls the Migrate command in the Python shell.
"""


class Migration(migrations.Migration):

    # If this were the first model we had created, one would see "initial = True" here, indicating the following model
    # is the first to have been created.

    # This portion of the code delineates all the models on which the one we are creating is dependent. It's
    # critical to be aware of these dependencies, especially if you decide to go on a cleaning spree and delete all
    # unused files. You might accidentally delete something you truly need.
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_city_country'),
    ]

    # This portion of the code creates the "Workout" model and includes all the specifications we listed in the
    # "models.py" file. The first line specifies what we want to call the model, while each of the subsequent lines
    # specify the fields the model will contain. Fields in this context are akin to the columns of a SQL database.
    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('sport', models.CharField(choices=[('Cycling', 'Cycling'), ('Hiking', 'Hiking'), ('Lifting Weights', 'Lifting Weights'), ('Running', 'Running'), ('Swimming', 'Swimming'), ('Walking', 'Walking'), ('Yoga', 'Yoga')], default='Running', max_length=15)),
                ('type', models.CharField(choices=[('Distance', 'Distance'), ('Interval', 'Interval'), ('None', 'None'), ('Race', 'Race'), ('Stress Relief', 'Stress Relief'), ('Workout', 'Workout')], default='None', max_length=15)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('workout_intensity', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Moderate'), ('Hard', 'Hard')], default='Medium', max_length=10)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
