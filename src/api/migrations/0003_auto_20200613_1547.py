# Generated by Django 3.0.7 on 2020-06-13 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200613_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='star',
            new_name='stars',
        ),
    ]
