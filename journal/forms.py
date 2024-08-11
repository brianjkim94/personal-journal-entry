from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import JournalEntry, Tag

class JournalEntryForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter tags (comma-separated)'}),
    )

    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'date', 'tags', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
        }

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', '')
        return tags

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tags = self.cleaned_data.get('tags', '')
        tag_names = [tag.strip() for tag in tags.split(',') if tag.strip()]
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        if commit:
            instance.save()
        return instance

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
