# Generated by Django 3.1.3 on 2021-01-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20210102_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, default='Not added...', max_length=500),
        ),
    ]