# Generated by Django 2.2.17 on 2020-12-28 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20201228_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]
