# Generated by Django 3.1.5 on 2021-01-21 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangout', '0002_hangout_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hangout',
            name='participants',
        ),
    ]