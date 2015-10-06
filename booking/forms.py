from django import forms
# a django module that creates forms
from .models import Delegate


class BookingForm(forms.ModelForm):
    class Meta:
        model = Delegate
        fields = ['delegate_name', 'delegate_surname', 'institution', 'country', 'dietary_requirements',
                  'other_requirements', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain = provider.split('.')
        extension = provider.split('.')
        return email

    def clean_delegate_name(self):
        delegate_name = self.cleaned_data.get('delegate_name')
        return delegate_name

    def clean_delegate_surname(self):
        delegate_surname = self.cleaned_data.get('delegate_surname')
        return delegate_surname

    def clean_institution(self):
        institution = self.cleaned_data.get('institution')
        return institution

    def clean_country(self):
        country = self.cleaned_data.get('country')
        return country

    def clean_dietary_requirements(self):
        dietary_requirements = self.cleaned_data.get('dietary_requirements')
        return dietary_requirements

    def clean_other_requirements(self):
        other_requirements = self.cleaned_data.get('other_requirements')
        return other_requirements


