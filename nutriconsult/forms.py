from django import forms
from django.contrib.auth.models import User
from .models import Client


# Create forms here
class AssistantRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Retype your password", widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match, please try again")
        return cd['password2']


class NutritionistRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Retype your password", widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match, please try again")
        return cd['password2']


class ClientRegistrationForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = ['first_name', 'last_name', 'birthday', 'sex', 'height', 'weight', 'exersice', 'nutritionist']
