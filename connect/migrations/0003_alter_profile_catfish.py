# Generated by Django 4.0.5 on 2022-06-23 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0002_alter_profile_catfish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='catfish',
            field=models.ManyToManyField(blank=True, null=True, related_name='catfish', to=settings.AUTH_USER_MODEL),
        ),
    ]
