# Generated by Django 2.0.13 on 2019-03-31 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20190331_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='allocated',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
