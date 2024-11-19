from django import forms
from django.contrib.auth.models import User

from notification.models import CustomUser


class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "full_name",
            "password",
            "role",
            "department",
            "position",
            "status",
        ]

    def save(self, commit=True):
        user_data = {
            key: self.cleaned_data[key] for key in ["username", "email", "full_name"]
        }
        user = User(**user_data)
        user.set_password(
            self.cleaned_data["password"]
        )  # Устанавливаем зашифрованный пароль
        if commit:
            user.save()

        custom_user = CustomUser(
            user=user,
            role=self.cleaned_data["role"],
            department=self.cleaned_data["department"],
            position=self.cleaned_data["position"],
            status=self.cleaned_data["status"],
        )
        custom_user.save()
        return custom_user
