from django import forms
from django.core import validators


def check_for_j(value):
    if value[0].lower() != 'j':
        raise forms.ValidationError('Name needs to start with J.')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_j])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        if email != v_email:
            raise forms.ValidationError('Make sure emails match.')



