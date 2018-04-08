# Generated by Django 2.0.3 on 2018-04-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_auto_20180408_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='elec_type',
            field=models.CharField(choices=[('pseg', 'PSE&G'), ('rockland', 'Orange Rockland Electric'), ('jcpl', 'Jersey Central Power & Light'), ('atlantic', 'Atlantic City Electric')], default='pseg', help_text='Your electric utility provider.', max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='elec_unit',
            field=models.CharField(choices=[('kWh', 'kWh')], default=('kWh', 'kWh'), max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gasoline_type',
            field=models.CharField(choices=[('e10', '10% Ethanol'), ('e0', 'Pure Gasoline'), ('diesel', 'Diesel'), ('b20', '20% Biodiesel')], default='e10', max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gasoline_unit',
            field=models.CharField(choices=[('gallon', 'gallons')], default=('gallon', 'gallons'), max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='heating_type',
            field=models.CharField(choices=[('gas', 'Natural Gas'), ('fuel', 'Fuel Oil'), ('elec', 'Electricity')], default='gas', max_length=40),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='heating_unit',
            field=models.CharField(choices=[('therm', 'therms'), ('gallon', 'gallons'), ('kWh', 'kWh')], default=('therm', 'therms'), max_length=40),
        ),
    ]
