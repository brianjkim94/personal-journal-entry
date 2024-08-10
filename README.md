# SEI SEBPT220 Project 4: DIGITAL JOURNAL

Digital Journal is an app that allows you to manage your journal entries or notes digitally. You can add a new entry with a title, content, date, tags and location. You can search for your entries by date or tag and also either edit or delete your saved entries. 

![Alt Text](./journal_project/images/Screenshot%202024-08-09%20at%208.57.33 PM.png)

# How it Works

User can sign up and start creating his or her journal entries with Digital Journal App. User can create, read, update and delete his or her personal journal entries. 
User can write add title, content, date and location when writing a new journal entry. Also the user can edit any of those attributes when updating the saved journal entry. 

![Alt Text](./journal_project/images/Screenshot%202024-08-09%20at%209.37.06 PM.png)

```py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import JournalEntry, Tag

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'date', 'tags', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple(),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),  # Free text input
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
```

# Technologies

- **PostgreSQL** 
- **Python** 
- **Django** 
- **HTML** 
- **CSS**
- **JavaScript**
- **GitHub**

## Links

[https://journal-project-6n06.onrender.com]()
[https://github.com/brianjkim94/personal-journal-entry]()


## User Stories
1. **View** 
    - User is able to view a list of all his or her saved journal entries.
2. **View a certain entry**
    - User is able to view the details of a specific journal entry so that he or she can read, edit or delete the entry.
3. **Create** 
    - User is able to create a new journal entry by filling out a form with a title, content, date, tags, and location.
4. **Edit** 
    - User is able to edit an existing journal entry so that he or she can make changes or updates to previous entries.
5. **Delete** 
    - User is able to delete a journal entry so that he or she can remove entries that are no longer needed.
6. **Search** 
    - User is able to search for journal entries by date or tag so that he or she can find specific entries easily.


## Models
1. **Tag**
    - Description: Represents a tag that can be associated with multiple journal entries. Tags are used to categorize or label journal entries for easier searching and filtering.
    - Fields: A CharField that stores the name of the tag.

2. **Location**
    - Description: Represents a location associated with a journal entry. 
    - Address: A CharField that stores a free-text address. 

3. **JournalEntry**
    - Description: Represents a single entry in the journal. This model stores the main content of the journal entry along with additional details such as date, tags, and location.
    - Title: A CharField that stores the title of the journal entry. It is limited to 200 characters and provides a brief description or header for the entry.
    - Content: A TextField that contains the main text or content of the journal entry. It can store large amounts of text.
    date: A DateField that records the date of the journal entry. It is used to organize and search entries by date.
    - Tags: A ManyToManyField that links to the Tag model, allowing each journal entry to be associated with multiple tags. This field is optional and can be left blank.
    - Location: A CharField that stores the location related to the journal entry. It allows for free-text input of the location address and is optional.

## Models.py Code Snippet
```py
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class JournalEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)  # Free text input field

    def __str__(self):
        return self.title
```

## Future Considerations

1. Advanced Search and Filtering
Consideration: Implement more advanced search features, such as filtering by date ranges, multiple tags, or specific keywords within the content.

2. Notification System
Consideration: Add a feature for notifications or reminder system that can send alerts or reminders for specific dates or tags (e.g., reminders for entries tagged with "Reminder").

3. Media Attachments
Consideration: Enable users to attach images, videos, or other media files to their journal entries. To have the user be more interactive with the app.
