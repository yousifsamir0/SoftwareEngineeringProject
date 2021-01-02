from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, FriendRequest


@receiver(post_save, sender=User)
# created = true when user is created
def auto_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, fName=instance.first_name, lName=instance.last_name)


# @receiver(post_save, sender=FriendRequest)
# def addfriend_relationship(sender, instance, created, **kwargs):
#   thesender = instance.sender
#  thereciever = instance.reciever
