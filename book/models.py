from django.db import models

class Book(models.Model):
    CHOICES = (
        ("DETECTIVE", "DETECTIVE"),
        ("ROMANS", "ROMANS")
    )

    title_book = models.CharField(max_length=999, null=True)
    image = models.ImageField(upload_to='')
    description = models.TextField(null=True, blank=True)
    type_book = models.TextField()
    genre = models.CharField(max_length=200, choices=CHOICES)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_book

