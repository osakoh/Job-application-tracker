# Generated by Django 2.2.17 on 2020-12-29 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20201229_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='job',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='jobs.Job'),
        ),
    ]
