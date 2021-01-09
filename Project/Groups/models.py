from django.db import models
from Profile.models import Profile
from django.template.defaultfilters import slugify
from random import randint


# Create your models here.


class Group(models.Model):

    name = models.CharField(max_length=50, blank=False)
    avatar = models.ImageField(
        default='avatars/groups/avatar.png', upload_to='avatars/groups/', blank=False)
    owner = models.ForeignKey(Profile, blank=False,
                              on_delete=models.CASCADE, related_name='myowngroups')
    description = models.TextField(max_length=500, blank=True)
    members = models.ManyToManyField(
        Profile, blank=True, related_name='mygroups')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug_flag = False
        slug = slugify(str(self.name))
        slug_flag = Group.objects.filter(
            slug=slug).exclude(name=self.name).exists()

        while slug_flag:
            slug = slugify(str(self.name) + str(randint(100, 999)))
            slug_flag = Group.objects.filter(slug=slug).exists()

        self.slug = slug
        super().save(*args, **kwargs)

    def get_posts(self):
        return self.groupposts.all()


class Grouprequest(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='groupsreqs')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='reqs')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'from {self.sender}to {self.group}'
