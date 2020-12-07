from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# When users sign up for FitHub, their information is stored in a table called "Profile." The class below
# called "Profile" inherits the Model class from Django and specifies all the attributes which belong to the "Profile"
# entity. The comments below explain which attributes of the table are created by a given section of code.


class Profile(models.Model):

	# Creates a foreign key constraint with the "User" model. A user can only have one profile, and a profile can
	# belong to only one user. When a user is deleted from the "User" model, their profile is deleted, too.
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# Creates a field to store user-uploaded profile pictures.
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	# Changes the picture size when uploaded to a suitable format.
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)  # Overrides image.

