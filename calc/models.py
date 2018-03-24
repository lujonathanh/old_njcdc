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
    CHILD_MULTIPLIER = 0.5

    ##############    GASOLINE    ##############

    # the fundamental unit: gasoline in gallons per month
    GASOLINE_CHOICES = (('e10', '10% Ethanol'), ('e0', 'Pure Gasoline'), ('diesel', 'Diesel'), ('b20', '20% Biodiesel'))
    gasoline_amt = models.FloatField(validators=[validate_nonnegative])
    gasoline_type = models.CharField(choices=GASOLINE_CHOICES, default='e10', max_length=6)

    # gallon of gas to tons of CO2
    # https://www.eia.gov/tools/faqs/faq.php?id=307&t=11
    GASOLINE_CO2_MULTIPLIER_DICT = {'e10': 17.6/2204.6, 'e0': 19.6/2204.6, 'diesel': 22.4/2204.6, 'biodiesel': 17.9/2204.6}


    ##############    ELECTRICITY    ##############

    # the fundamental unit: electricity in kWh per month
    ELEC_CHOICES = ( ('pseg', 'PSE&G'), ('rockland', 'Orange Rockland Electric'),
                     ('jcpl', 'Jersey Central Power & Light'), ('atlantic', 'Atlantic City Electric'))
    elec_amt = models.FloatField(validators=[validate_nonnegative])
    elec_type = models.CharField(choices=ELEC_CHOICES, default='pseg', max_length=8)

    ELEC_CO2_MULTIPLIER_DICT = {'pseg': 0.0003441034104, 'rockland': 0.0004169606023, 'jcpl': 0.0004644724986, 'atlantic': 0.0004626444685}

    ##############    HEATING    ##############

    # the fundamental unit: therm for gas, gallons for fuel oil, kWh for elec
    HEATING_CHOICES = ( ('gas', 'Natural Gas'), ('fuel', 'Fuel Oil'), ('elec', 'Electricity'))
    heating_amt = models.FloatField(validators=[validate_nonnegative])
    heating_type = models.CharField(choices=HEATING_CHOICES, default='gas', max_length=4)
    HEATING_UNITS_DICT = {'gas': 'therm', 'fuel': 'gallon', 'elec': 'kWh'}

    # Natural Gas CO2/therm: https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references
    # Fuel Oil CO2/gallon
    # note everything should be converted to BTU soon.

    # TODO: fix electricity
    HEATING_CO2_MULTIPLIER_DICT = {'gas': 0.0053, 'fuel': GASOLINE_CO2_MULTIPLIER_DICT['diesel'], 'elec': 0.3}
    # HEATING_CO2_MULTIPLIER_DICT = {'gas': 0.0053, 'fuel': GASOLINE_CO2_MULTIPLIER_DICT['diesel'], 'elec': ELEC_CO2_MULTIPLIER_DICT[str(elec_type)]}




    def calculate_net(self):
        # TODO: update. remember should be monthly. should calculate with child as well
        REVENUEPERADULT = self.fee * 10
        self.DIVIDENDPERADULT =  REVENUEPERADULT * self.rebate_portion
        self.benefit = (self.CHILD_MULTIPLIER * self.children + self.adults) * self.DIVIDENDPERADULT



        self.gasoline_cost = self.GASOLINE_CO2_MULTIPLIER_DICT[self.gasoline_type] * self.gasoline_amt


        self.elec_cost = self.ELEC_CO2_MULTIPLIER_DICT[self.elec_type] * self.elec_amt

        self.heating_cost = self.HEATING_CO2_MULTIPLIER_DICT[self.heating_type] * self.heating_amt

        self.total_cost = self.gasoline_cost + self.elec_cost + self.heating_cost

        self.net = self.benefit - self.total_cost






