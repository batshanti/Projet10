# Generated by Django 3.1.4 on 2022-08-12 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0005_contributors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('IMPROVEMENT', 'IMPROVEMENT'), ('TASK', 'TASK')], max_length=12)),
                ('priority', models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], max_length=12)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('TODO', 'TODO'), ('IN_PROGRESS', 'IN_PROGRESS'), ('DONE', 'DONE')], max_length=12)),
                ('assignee_user_id', models.ForeignKey(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL), on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='project.projects')),
            ],
        ),
    ]
