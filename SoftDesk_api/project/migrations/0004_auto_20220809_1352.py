# Generated by Django 3.1.4 on 2022-08-09 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20220809_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='author_id',
            new_name='author',
        ),
    ]
