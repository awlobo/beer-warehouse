from django import forms


class CompanyForm(forms.Form):
    name = forms.CharField(required=True)
    tax_number = forms.IntegerField(required=True, label="tax no.", initial=0)
