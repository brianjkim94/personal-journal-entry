from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%m/%d/%Y')

class JournalEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.OneToOneField(Date, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
