from django.db import models

# Create your models here.

class Quotes(models.Model):
    quote_text = models.TextField()
    author = models.CharField(max_length=255, blank='True')

    def __str__(self):
        if self.author:
            return f"{self.quote_text} - {self.author}"
        else:
            return self.quote_text[:50] + '...'
