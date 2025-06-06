import re

from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Benutzername"))
    password = forms.CharField(label=_("Passwort"), widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(
        validators=[MaxLengthValidator(50)], label=_("Vorname")
    )
    last_name = forms.CharField(
        validators=[MaxLengthValidator(50)], label=_("Nachname")
    )
    username = forms.CharField(
        validators=[MaxLengthValidator(50)], label=_("Benutzername")
    )
    email = forms.EmailField(
        validators=[MaxLengthValidator(50)], label=_("E-Mail Adresse")
    )
    password = forms.CharField(widget=forms.PasswordInput(), label=_("Passwort"))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        help_texts = {"username": ""}
        error_messages = {"name": {"required": "Pflichtfeld"}}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Username ist ein Pflichtfeld")
        if " " in username:
            raise forms.ValidationError(
                "Benutzername darf weder Sonderzeichen, Lücken, noch Grossbuchstaben enthalten."
            )
        if not re.match("^[a-z0-9_.]+$", username):
            raise forms.ValidationError(
                "Benutzername darf weder Sonderzeichen, Lücken, noch Grossbuchstaben enthalten."
            )
        return username.lower()

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
