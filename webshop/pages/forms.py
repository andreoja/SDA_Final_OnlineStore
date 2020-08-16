from django import forms
from django.contrib.auth.forms import UserCreationForm
from pages.models import StoreUser

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    company_name = forms.CharField()
    registration_number = forms.CharField()
    VAT_number = forms.CharField()
    address = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(render_value=True))

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError(
                "password and password confirmation does not match"
            )

        username = cleaned_data.get('username')
        existing_user = StoreUser.objects.filter(username=username)

        if existing_user.count() != 0:
            raise forms.ValidationError(
                "This username is already taken. Choose another one"
            )