from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from random import randint
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    eMail = models.CharField(max_length=50)
    avatar = models.ImageField(
        default='avatars/avatar.png', upload_to='avatars/', blank=False)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    about = models.TextField(
        blank=True, max_length=300, default='Not added...')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}---{self.created}'

    def get_name(self):
        return f'{self.fName} {self.lName}'

    def get_friends_num(self):
        return self.friends.all().count()

    def get_friends(self):
        return self.friends.all()

    def get_posts(self):
        return self.posts.all()

    def save(self, *args, **kwargs):
        slug_flag = False

        if self.fName and self.lName:
            slug = slugify(str(self.fName) + '-' + str(self.lName))
            slug_flag = Profile.objects.exclude(
                user=self.user).filter(slug=slug).exists()
            #slug_flag = Profile.objects.filter(slug=slug).exists()

            while slug_flag:
                slug = slugify(str(self.fName) + '-' +
                               str(self.lName)+'-' + str(randint(100, 999)))
                slug_flag = Profile.objects.filter(slug=slug).exists()
        else:
            slug = str(self.user.username)
        self.slug = slug
        super().save(*args, **kwargs)


class FriendRequest(models.Model):

    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='reciever')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'from {self.sender}to {self.reciever}'
