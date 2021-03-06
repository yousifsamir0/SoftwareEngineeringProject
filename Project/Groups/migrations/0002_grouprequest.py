# Generated by Django 3.1.4 on 2021-01-06 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_auto_20210102_2205'),
        ('Groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouprequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reqs', to='Groups.group')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupsreqs', to='Profile.profile')),
            ],
        ),
    ]
