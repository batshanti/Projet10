from django.db import models
from django.contrib.auth.models import User


TYPES = [
    ('BACKEND', 'BACKEND'),
    ('FRONTEND', 'FRONTEND'),
    ('iOS', 'iOS'),
    ('ANDROID', 'ANDROID')
]

PERMISSION = [
    ('restricted', 'restricted'),
    ('all', 'all'),
]

ROLE = [
    ('author', 'author'),
    ('responsable', 'responsable'),
    ('Contributor', 'Contributor')
]


class Projects(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(choices=TYPES, max_length=16)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author'
    )

    def __str__(self):
        return self.title


class Contributors(models.Model):

    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    projet_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    permission = models.CharField(max_length=50, choices=PERMISSION, default='restricted')
    role = models.CharField(max_length=128, choices=ROLE, default="")
