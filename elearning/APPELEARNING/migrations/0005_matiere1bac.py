# Generated by Django 5.0.6 on 2025-01-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APPELEARNING", "0004_remove_utilisateur_niveau_utilisateur_groups_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matiere1Bac",
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
                ("nom", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
