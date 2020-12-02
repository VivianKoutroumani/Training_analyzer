from django.db import migrations


"""
This migration was generated when we decided we no longer needed the dummy data that was recorded in these two
tables. We were able to delete "City" and "Country" because we had successfully integrated the "Workout" table into
the FitHub platform. Therefore, the group member in charge of graphs was able to access and analyze real data.
"""


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_workout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
