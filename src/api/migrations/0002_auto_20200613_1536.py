# Generated by Django 3.0.7 on 2020-06-13 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='start',
            new_name='star',
        ),
    ]