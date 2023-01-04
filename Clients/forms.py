from ckeditor.widgets import CKEditorWidget
from django import forms

from Clients.models import ClientProfile, ClientJob, JobComment


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
            'pi_link': 'Pinterest Link', 'pp_link': 'Personal Website Link',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'establishment': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),  # forms.CharField(widget=CKEditorWidget()),
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
        super(ClientProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget = CKEditorWidget()


class ClientJobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientJobForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'value': self.instance.title})

    class Meta:
        model = ClientJob
        fields = [
            'title', 'description', 'budget', 'date_due', 'is_available',
        ]
        labels = {
            'title': 'Title', 'description': 'Description', 'budget': 'Budget', 'date_due': 'Deadline',
            'is_available': 'Available',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': '3'}),
        }


class JobCommentForm(forms.ModelForm):
    class Meta:
        model = JobComment
        fields = [
            'comment',
        ]
        labels = {
            'comment': 'Add Comment  ',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': '3', 'placeholder': 'Opinions, Ideas, Suggestions ... etc'}),
        }
