from django.db import models
from django.core.validators import FileExtensionValidator
from Profile.models import Profile
from Groups.models import Group

# Create your models here.


class Post(models.Model):

    body = models.TextField(blank=True, max_length=500)
    image = models.ImageField(upload_to='postsimages/', blank=True,
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')
    liked_by = models.ManyToManyField(
        Profile, blank=True, related_name='liked_posts')
    created = models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True,related_name='groupposts')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body[:16]}"

    def get_liked_by(self):
        return self.liked_by.all()

    def get_comments(self):
        return self.comments.all()

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    body = models.TextField(max_length=250, blank=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        ordering = ('-created',)
