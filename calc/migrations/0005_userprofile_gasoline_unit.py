# Generated by Django 2.0.3 on 2018-04-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20180404_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gasoline_unit',
            field=models.CharField(choices=[('gallon', 'gallons')], default=('gallon', 'gallons'), max_length=6),
        ),
    ]
