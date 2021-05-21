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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=500, blank=True, null=True)
    comment = models.TextField(max_length=2500, blank=True, null=True)
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user.username
