from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.CharField(max_length=50)
    crated_At = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "blog"

    def __str__(self):
        return self.title
