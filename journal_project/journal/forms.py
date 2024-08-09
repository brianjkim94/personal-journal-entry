from django import forms
from .models import JournalEntry, Tag, Location

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'date', 'tags', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple(),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location address here'}), 
        }
