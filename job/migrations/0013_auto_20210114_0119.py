# Generated by Django 3.1.5 on 2021-01-14 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_auto_20210113_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='apply',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
