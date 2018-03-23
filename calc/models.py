from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

#################         VALIDATORS          #################

def validate_nonnegative(value):
    if value < 0:
        raise ValidationError(_('%(value)s is a negative number'),
            params={'value': value},
        )

def validate_0to1(value):
    if value < 0:
        raise ValidationError(_('%(value)s is a negative number'),
                    params={'value': value},
                )
    if value > 1:
        raise ValidationError(_('%(value)s is a negative number'),
                    params={'value': value},
                )


#################         MODELS         #################


class UserProfile(models.Model):
    fee = models.FloatField(default=30., validators=[validate_nonnegative])
    rebate_portion = models.FloatField(default=0.7, validators=[validate_0to1])
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()

    # the fundamental unit: gasoline in gallons per month
    gasoline_amt = models.FloatField(validators=[validate_nonnegative])

    # the fundamental unit: therm for gas, gallons for fuel oil, kWh for elec
    HEATING_CHOICES = ( ('gas', 'Natural Gas'), ('fuel', 'Fuel Oil'), ('elec', 'Electricity'))
    heating_amt = models.FloatField(validators=[validate_nonnegative])
    heating_type = models.CharField(choices=HEATING_CHOICES, default='gas', max_length=4)

    # the fundamental unit: electricity in kWh per month
    ELEC_CHOICES = ( ('pseg', 'PSE&G'), ('rockland', 'Orange Rockland Electric'),
                     ('jcpl', 'Jersey Central Power & Light'), ('atlantic', 'Atlantic City Electric'))
    elec_amt = models.FloatField(validators=[validate_nonnegative])
    elec_type = models.CharField(choices=ELEC_CHOICES, default='pseg', max_length=8)





