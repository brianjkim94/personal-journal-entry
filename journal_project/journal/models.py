from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()  # Ensure this is correct
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
