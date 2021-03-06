# Generated by Django 2.0.13 on 2019-03-31 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_school_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.CharField(max_length=100)),
                ('endTime', models.CharField(max_length=100)),
                ('allocated', models.CharField(default=None, max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
        migrations.AddField(
            model_name='prospective',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Request'),
        ),
    ]
