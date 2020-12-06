from django.db.models.signals import post_save #signal that gets fired when object is saved
from django.contrib.auth.models import User #sender of signal
from django.dispatch import receiver # receiver of signal
from .models import Profile 

#Creating profile when user is created

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
		instance.profile.save()

