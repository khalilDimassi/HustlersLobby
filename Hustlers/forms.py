from ckeditor.widgets import CKEditorWidget
from django import forms

from Hustlers.models import HustlerProfile

LANGUAGE_CHOICES = (
    ('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian'), ('pt', 'Portuguese'),
    ('ru', 'Russian'), ('zh', 'Chinese'), ('ja', 'Japanese'), ('ko', 'Korean'), ('ar', 'Arabic'), ('hi', 'Hindi'),
    ('bn', 'Bengali'), ('pa', 'Punjabi'), ('ta', 'Tamil'), ('te', 'Telugu'), ('ur', 'Urdu'), ('vi', 'Vietnamese'),
    ('id', 'Indonesian'), ('ms', 'Malay'), ('th', 'Thai'), ('tr', 'Turkish'), ('pl', 'Polish'), ('nl', 'Dutch'),
    ('sv', 'Swedish'), ('da', 'Danish'), ('no', 'Norwegian'), ('fi', 'Finnish'), ('el', 'Greek'), ('he', 'Hebrew'),
    ('hu', 'Hungarian'), ('ro', 'Romanian'), ('cs', 'Czech'), ('sk', 'Slovak'), ('sl', 'Slovenian'),
    ('uk', 'Ukrainian'),
)


class HustlerProfileForm(forms.ModelForm):
    class Meta:
        model = HustlerProfile
        fields = [
            'first_name', 'last_name', 'profession', 'establishment', 'birth_date', 'profile_picture', 'bio',
            'phone_number', 'skills', 'languages',
            'fb_link', 'tw_link', 'gh_link', 'li_link', 'ig_link', 'pi_link', 'pp_link',
        ]
        labels = {
            'first_name': 'First Name', 'last_name': 'Last Name',
            'profession': 'Profession', 'establishment': 'Establishment',
            'birth_date': 'Birth Date', 'profile_picture': 'Profile Picture',
            'bio': 'Bio', 'phone_number': 'Phone Number', 'skills': 'Skill set', 'languages': 'Spoken Languages',
            'fb_link': 'Facebook Link', 'tw_link': 'Twitter Link', 'gh_link': 'Github Link', 'li_link': 'LinkedIn Link',
            'ig_link': 'Instagram Link', 'pi_link': 'Pinterest Link', 'pp_link': 'Personal Website Link',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'establishment': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),  # forms.CharField(widget=CKEditorWidget()),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'languages': forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_link': forms.TextInput(attrs={'class': 'form-control'}),
            'tw_link': forms.TextInput(attrs={'class': 'form-control'}),
            'gh_link': forms.TextInput(attrs={'class': 'form-control'}),
            'li_link': forms.TextInput(attrs={'class': 'form-control'}),
            'ig_link': forms.TextInput(attrs={'class': 'form-control'}),
            'pi_link': forms.TextInput(attrs={'class': 'form-control'}),
            'pp_link': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(HustlerProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget = CKEditorWidget()
