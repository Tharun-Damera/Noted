# Generated by Django 4.1.7 on 2023-04-23 09:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notesapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="archive",
            name="edit_date",
        ),
        migrations.RemoveField(
            model_name="archive",
            name="publish_date",
        ),
        migrations.RemoveField(
            model_name="notes",
            name="edit_date",
        ),
        migrations.RemoveField(
            model_name="notes",
            name="publish_date",
        ),
        migrations.RemoveField(
            model_name="trash",
            name="edit_date",
        ),
        migrations.RemoveField(
            model_name="trash",
            name="publish_date",
        ),
    ]
