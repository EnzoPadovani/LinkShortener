from django.db import models

# recebe o Link
class Link(models.Model):
    linkOriginal = models.URLField()
    linkKey = models.CharField(max_length= 16, unique=True)

    def __str__(self) -> str:
        return self.linkKey
    