from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

