# Generated by Django 4.0.6 on 2022-07-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0033_remove_post_name_of_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='previous_companies',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
