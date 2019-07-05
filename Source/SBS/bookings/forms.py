from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_shortname',
                  'company_longname',
                  'company_registration',
                  'company_addressline1',
                  'company_addressline2',
                  'company_addressline3',
                  'company_addressline4',
                  'company_state',
                  'company_postalcode',
                  'company_country',
                  'company_default',
                  'is_active']
