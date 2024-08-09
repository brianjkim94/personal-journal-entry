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
