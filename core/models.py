from django.db import models

class Bookmark(models.Model):
    title = models.CharField(verbose_name = "Title", max_length= 150)

    class Meta:
            verbose_name = "Bookmark"
            verbose_name_plural = "Bookmarks"
    
    def __str__(self):
        return self.title
