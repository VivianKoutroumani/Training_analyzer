from django.db import migrations, models


"""
This automatic migration was generated as a part of our continued quest to understand how the Django platform works.
Specifically, this migration added two fields to the "Posts" model, both of which allowed us to first record and then
manipulate dummy data on the FitHub site. These two fields—workout distance and workout time—afforded us the opportunity
to create the respective frameworks we ended up using for both the "Overview" and "User Posts" views. 
"""


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='workout_distance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='workout_time',
            field=models.IntegerField(default=0),
        ),
    ]
