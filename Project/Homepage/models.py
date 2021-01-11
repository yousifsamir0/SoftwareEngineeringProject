from django.db import models

# Create your models here.


class Clup(models.Model):
    logo = models.ImageField(
        default='Clups/clup.png', upload_to='Clups/', blank=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Match(models.Model):

    leftteam = models.ForeignKey(
        Clup, blank=False, on_delete=models.CASCADE, related_name="left_team")
    rightteam = models.ForeignKey(
        Clup, blank=False, on_delete=models.CASCADE, related_name="right_team")
    left_team_score = models.CharField(max_length=2, blank=False)
    right_team_score = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return f"{self.leftteam}-{self.left_team_score}-{self.right_team_score}-{self.rightteam}"
