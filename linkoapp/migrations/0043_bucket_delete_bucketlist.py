# Generated by Django 4.0.6 on 2022-07-18 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0042_bucketlist_userp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('userP', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='linkoapp.portrait')),
            ],
        ),
        migrations.DeleteModel(
            name='BucketList',
        ),
    ]
