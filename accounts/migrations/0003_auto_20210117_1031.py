# Generated by Django 3.1.5 on 2021-01-17 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210117_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_nmuber',
            new_name='phone_number',
        ),
    ]