# Generated by Django 3.0.3 on 2020-05-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='workprogres',
        ),
        migrations.AddField(
            model_name='user',
            name='desg',
            field=models.CharField(default='B', max_length=250),
        ),
        migrations.AddField(
            model_name='work',
            name='Workprogres',
            field=models.CharField(default='B', max_length=25),
            preserve_default=False,
        ),
    ]
