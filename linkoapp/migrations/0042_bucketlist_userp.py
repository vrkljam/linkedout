# Generated by Django 4.0.6 on 2022-07-18 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0041_remove_bucketlist_userfk'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='userP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='linkoapp.portrait'),
        ),
    ]
