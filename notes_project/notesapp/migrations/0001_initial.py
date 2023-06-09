# Generated by Django 4.1.7 on 2023-04-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("note", models.TextField()),
                ("publish_date", models.DateField()),
                ("edit_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Notes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("note", models.TextField()),
                ("publish_date", models.DateField()),
                ("edit_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Trash",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("note", models.TextField()),
                ("publish_date", models.DateField()),
                ("edit_date", models.DateField()),
            ],
        ),
    ]
