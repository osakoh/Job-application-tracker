# Generated by Django 2.2.17 on 2020-12-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20201228_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_applied',
            field=models.DateField(null=True),
        ),
    ]
