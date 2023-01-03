from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)


class RegistrationForm(forms.Form):
    ROLE_CHOICES = [
        ('Clients', 'Client'),
        ('Hustlers', 'Hustler'),
    ]
    username = forms.CharField(
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label_suffix='',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(
        label_suffix='',
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-select-input'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class EditSettingsForm(UserChangeForm):
    password = None
    username = forms.CharField(
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label_suffix='',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        user = kwargs['instance']
        super().__init__(*args, **kwargs)
        # init inputs
        self.initial['username'] = user.username
        self.initial['email'] = user.email

    class Meta:
        model = User
        fields = ('username', 'email')


class EditPasswordForm(forms.Form):
    old_password = forms.CharField(
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password_confirm = forms.CharField(
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'new_password_confirm')

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        new_password_confirm = cleaned_data.get("new_password_confirm")
        if new_password and new_password_confirm and new_password != new_password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, user):
        user.set_password(self.cleaned_data['new_password'])
        user.save()
        return user
