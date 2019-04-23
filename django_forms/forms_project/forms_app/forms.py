from django import forms
from forms_app.models import NewPerson, UserProfileInfo
from django.core import validators


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


class FormNewPerson(forms.ModelForm):
    """Linked to NewPerson model."""

    class Meta:
        model = NewPerson
        fields = '__all__'


class FormUserProfileInfo(forms.ModelForm):
    """Extension of django's User model."""
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfo
        exclude = ('user',)
