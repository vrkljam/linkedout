# Generated by Django 4.0.6 on 2022-07-15 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0032_bucketlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name_of_user',
        ),
    ]