from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django import forms

from users import models


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label=_("username"),
        widget=forms.TextInput(
            attrs={"class": "form-input form-control", "placeholder": _("username")}
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-input form-control", "placeholder": _("Password")}
        ),
    )
    password2 = forms.CharField(
        label=_("Password2"),
        widget=forms.PasswordInput(
            attrs={"class": "form-input form-control", "placeholder": _("Password2")}
        ),
    )

    class Meta:
        model = models.User  # noqa E501
        fields = ["first_name", "last_name", "username", "password1", "password2"]
        labels = {
            "first_name": _("First name"),
            "last_name": _("Last name"),
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": _("First name"),
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": _("Last name"),
                }
            ),
        }


class UserEditForm(forms.ModelForm):
    username = forms.CharField(
        label=_("username"),
        widget=forms.TextInput(
            attrs={"class": "form-input form-control", "placeholder": _("username")}
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-input form-control", "placeholder": _("Password")}
        ),
    )
    password2 = forms.CharField(
        label=_("Password2"),
        widget=forms.PasswordInput(
            attrs={"class": "form-input form-control", "placeholder": _("Password2")}
        ),
    )

    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "username", "password1", "password2"]

        labels = {
            "first_name": _("First name"),
            "last_name": _("Last name"),
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": _("First name"),
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": _("Last name"),
                }
            ),
        }
