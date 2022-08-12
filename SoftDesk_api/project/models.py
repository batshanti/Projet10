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

PRIORITY = [
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGH', 'HIGH')
]

TAG = [
    ('BUG', 'BUG'),
    ('IMPROVEMENT', 'IMPROVEMENT'),
    ('TASK', 'TASK')
]

STATUS = [
    ('TODO', 'TODO'),
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('DONE', 'DONE')
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


class Issues(models.Model):

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)
    tag = models.CharField(max_length=12, choices=TAG)
    priority = models.CharField(max_length=12, choices=PRIORITY)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS)

    project_id = models.ForeignKey(
        to=Projects,
        on_delete=models.CASCADE,
        related_name='issues'
    )

    author_user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='issue_author'
    )

    assignee_user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        default=author_user_id,
        related_name='issue_assignee'
    )
