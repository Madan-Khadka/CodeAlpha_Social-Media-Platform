from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


# ============================================================
# REGISTRATION FORM
# ============================================================

class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                "This username is already taken."
            )

        return username


# ============================================================
# PROFILE EDIT FORM
# ============================================================

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            "bio",
            "profile_picture",
        ]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Write something about yourself...",
                }
            ),
        }


# ============================================================
# USER INFORMATION FORM
# ============================================================

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First name",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email address",
                }
            ),
        }