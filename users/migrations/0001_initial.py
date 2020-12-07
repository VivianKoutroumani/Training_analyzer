from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


"""
This migration creates a model called "Profile." It is thanks to this model that we were eventually able to store
information about users such as their username, email address, and password. We also give users the opportunity to add
personality to their profile by uploading a customized profile picture. This image is what's shown next to all the
activities they post on the platform.
"""


class Migration(migrations.Migration):

    # Indicates that this is the first model to be created within the "users" application.
    initial = True

    # This dependency allows us to perform password validation for each profile upon log-in.
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(

            # Establishes the name of the model. This in essence is the name of the table, too.
            name='Profile',
            fields=[

                # These lines specify facts about the table's design, like which attribute is its primary key as well
                # as whether that primary key should auto-increment.
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                # This line manages the profile pictures users upload to their profiles, telling the program where they
                # should be stored.
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),

                # Specifies that if a user is deleted from the "Profile" table, all the information associated with them
                # should be deleted, too.
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
