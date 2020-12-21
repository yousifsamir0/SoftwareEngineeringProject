from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship


@receiver(post_save, sender=User)
# created = true when user is created
def auto_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Relationship)
def addfriend_relationship(sender, instance, created, **kwargs):
    thesender = instance.sender
    thereciever = instance.reciever
    if instance.stutus == 'Accepted':
        thesender.friends.add(thereciever.user)
        thereciever.friends.add(thesender.user)
        thesender.save()
        thereciever.save()
