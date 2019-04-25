from django import forms
from django.core import validators
from django.contrib.auth.models import User
from forms_app.models import UserProfileInfo


def check_for_j(value):
    if value[0].lower() != 'j':
        raise forms.ValidationError('Name needs to start with J.')


class FormName(forms.Form):
    """Test form not linked to a model."""
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


class FormUser(forms.ModelForm):
    """Linked to django User."""

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class FormUserProfileInfo(forms.ModelForm):
    """Extension of django's User model."""

    class Meta:
        model = UserProfileInfo
        fields = ('user', 'portfolio', 'picture')
