# Generated by Django 4.2.14 on 2024-07-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
