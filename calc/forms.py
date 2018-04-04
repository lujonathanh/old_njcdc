from django import forms
from .models import UserProfile


# TODO
class InputForm(forms.ModelForm):
    #fee = forms.FloatField(label="Fee", error_messages={'invalid': "Something invalid."})

    class Meta:
        model = UserProfile
        fields = ('fee', 'rebate_portion', 'adults', 'children', 'gasoline_type', 'gasoline_amt', 'gasoline_unit',
                  'heating_type', 'heating_amt', 'heating_unit',
                  'elec_type', 'elec_amt',  'elec_unit')
        # fields1 = ('zip', 'adults', 'children', 'fee', 'rebate_portion')
        # fields2 = ('gasoline_amt', 'gasoline_type',
        #           'heating_amt', 'heating_type',
        #           'elec_amt', 'elec_type')