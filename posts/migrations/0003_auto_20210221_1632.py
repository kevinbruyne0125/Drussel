# Generated by Django 3.1.6 on 2021-02-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210221_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='viewed',
            field=models.DateTimeField(null=True),
        ),
    ]
