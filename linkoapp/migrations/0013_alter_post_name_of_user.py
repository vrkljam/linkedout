# Generated by Django 4.0.6 on 2022-07-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0012_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name_of_user',
            field=models.CharField(max_length=50),
        ),
    ]
