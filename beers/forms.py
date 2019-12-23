from django import forms

# class CompanyForm(forms.Form):
#     name = forms.CharField(required=True)
#     tax_number = forms.IntegerField(required=True, label="tax no.", initial=0)
from beers.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_at', 'created_by', 'last_modified_by']
