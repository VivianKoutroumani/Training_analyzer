from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


"""
This migration creates a model called "Posts." This model was used as a test case for us to experience the Django
platform and understand how it works. Specifically, creating this model illustrated for us the Model -> Make migrations
-> Migrate pathway, which was critical to our correctly implementing the workout model later on. For a detailed
explanation as to how models works, see the "0004_workouts.py" file. (Note: we did not remove this model
due to dependency concerns.)
"""


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
