# Generated by Django 4.0.6 on 2022-07-18 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0036_bucketlist_user_alter_bucketlist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkoapp.portrait'),
        ),
    ]
