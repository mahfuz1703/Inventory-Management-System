# Generated by Django 3.0.3 on 2020-04-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200401_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='total',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
