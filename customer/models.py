from django.db import models
from django.contrib.auth.models import User


RATING_CHOICES = [
    (1, '1 - Awful'),
    (2, '2 - Could be Better'),
    (3, '3 - OK'),
    (4, '4 - Good'),
    (5, '5 - Amazing'),
]


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=500, blank=True)
    comment = models.TextField(max_length=2500, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
