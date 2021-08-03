from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='image/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
