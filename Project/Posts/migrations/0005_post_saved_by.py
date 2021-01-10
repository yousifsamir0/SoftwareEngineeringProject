# Generated by Django 3.1.3 on 2021-01-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_auto_20210102_2205'),
        ('Posts', '0004_auto_20210105_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='savedposts', to='Profile.Profile'),
        ),
    ]