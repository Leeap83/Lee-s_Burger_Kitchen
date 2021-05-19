from django.db import models
from django.contrib.auth.models import User


RATING_CHOICES = [
    (1, '1/5'),
    (2, '2/5 '),
    (3, '3/5'),
    (4, '4/5'),
    (5, '5/5'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=500, blank=True)
    comment = models.TextField(max_length=2500, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
