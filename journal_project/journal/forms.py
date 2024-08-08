from django import forms
from .models import JournalEntry, Tag

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'date', 'tags']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
