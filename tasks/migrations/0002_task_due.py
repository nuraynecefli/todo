# Generated by Django 3.2.21 on 2023-10-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
