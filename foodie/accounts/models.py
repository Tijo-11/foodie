from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    bio = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(
        upload_to='profile/', 
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new profile if a new user is created
        UserProfile.objects.create(user=instance)
    else:
        # Save existing profile on update
        instance.profile.save()
