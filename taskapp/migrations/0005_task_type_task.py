# Generated by Django 2.0.7 on 2018-08-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_auto_20180801_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type_task',
            field=models.IntegerField(default=0),
        ),
    ]