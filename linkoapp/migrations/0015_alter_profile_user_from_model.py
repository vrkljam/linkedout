# Generated by Django 4.0.6 on 2022-07-12 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkoapp', '0014_rename_testing_profile_user_from_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_from_model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
