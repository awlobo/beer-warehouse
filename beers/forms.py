from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

# class CompanyForm(forms.Form):
#     name = forms.CharField(required=True)
#     tax_number = forms.IntegerField(required=True, label="tax no.", initial=0)
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from beers.models import Company, Beer


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_at', 'created_by', 'last_modified_by', 'last_modified_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = "company-form"
        self.helper.form_class = "blue"
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_method = 'post'
        self.helper.form_action = ""

        self.helper.add_input(Submit('submit-name', 'Save'))

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == "pablo":
            raise ValidationError("Name forbidden", code="invalid")
        return name

    def clean_tax_number(self):
        tax = self.cleaned_data['tax_number']
        if tax <= 0:
            raise ValidationError("Tax forbidden", code="invalid")
        return tax

    def clean(self):
        cleaned_data = super().clean()
        tax = self.cleaned_data.get('tax_number')
        name = self.cleaned_data.get('name')

        if name == "pepe" and tax > 3:
            # raise ValidationError("DANGER", code="invalid")
            self.add_error('tax_number', 'muy mal')


class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        exclude = ['created_at', 'created_by', 'last_modified_by', 'last_modified_at']


BeerFormset = inlineformset_factory(Company, Beer, form=BeerForm, extra=1)
