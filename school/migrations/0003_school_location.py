# Generated by Django 2.0.13 on 2019-03-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_school_credentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
