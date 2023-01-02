from django import forms


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
