# Generated by Django 4.2.8 on 2024-01-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='label',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]