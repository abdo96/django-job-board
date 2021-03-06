# Generated by Django 3.1.5 on 2021-01-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20210112_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
