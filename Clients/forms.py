from django import forms

from Clients.models import ClientProfile


class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = [
            'first_name', 'last_name', 'profession', 'establishment', 'birth_date', 'profile_picture', 'bio',
            'phone_number', 'fb_link', 'tw_link', 'gh_link', 'li_link', 'ig_link', 'pi_link', 'pp_link',
        ]
        labels = {
            'first_name': 'First Name', 'last_name': 'Last Name',
            'profession': 'Profession', 'establishment': 'Establishment',
            'birth_date': 'Birth Date', 'profile_picture': 'Profile Picture',
            'bio': 'Bio', 'phone_number': 'Phone Number', 'fb_link': 'Facebook Link', 'tw_link': 'Twitter Link',
            'gh_link': 'Github Link', 'li_link': 'LinkedIn Link', 'ig_link': 'Instagram Link',
            'pi_link': 'Pinterest Link', 'pp_link': 'Website Link',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'establishment': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'fb_link': forms.URLInput(attrs={'class': 'form-control'}),
            'tw_link': forms.URLInput(attrs={'class': 'form-control'}),
            'gh_link': forms.URLInput(attrs={'class': 'form-control'}),
            'li_link': forms.URLInput(attrs={'class': 'form-control'}),
            'ig_link': forms.URLInput(attrs={'class': 'form-control'}),
            'pi_link': forms.URLInput(attrs={'class': 'form-control'}),
            'pp_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        profession = cleaned_data.get('profession')
        establishment = cleaned_data.get('establishment')
        birth_date = cleaned_data.get('birth_date')
        profile_picture = cleaned_data.get('profile_picture')
        bio = cleaned_data.get('bio')
        phone_number = cleaned_data.get('phone_number')
        fb_link = cleaned_data.get('fb_link')
        tw_link = cleaned_data.get('tw_link')
        gh_link = cleaned_data.get('gh_link')
        li_link = cleaned_data.get('li_link')
        ig_link = cleaned_data.get('ig_link')
        pi_link = cleaned_data.get('pi_link')
        pp_link = cleaned_data.get('pp_link')
        
        cleaned_data = {
            'first_name': first_name, 'last_name': last_name, 'profession': profession,
            'establishment': establishment, 'birth_date': birth_date, 'profile_picture': profile_picture,
            'bio': bio, 'phone_number': phone_number, 'fb_link': fb_link, 'tw_link': tw_link,
            'gh_link': gh_link, 'li_link': li_link, 'ig_link': ig_link, 'pi_link': pi_link,
            'pp_link': pp_link,
        }
        return cleaned_data
