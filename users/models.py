from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs): #change picture size when uplodaed
		super(Profile, self).save(*args, **kwargs) # change of original program -> Solution found on stackOVerflow: https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert

		img = Image.open(self.image.path)

		if img.height > 300 or img.width >300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path) #overriding image






# Create your models here.
