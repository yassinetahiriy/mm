# Generated by Django 5.0.6 on 2025-01-03 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APPELEARNING", "0008_remove_matiere1bac_cours_cours"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cours1bac",
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
                ("titre", models.CharField(max_length=255)),
                (
                    "matiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cours",
                        to="APPELEARNING.matiere1bac",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Cours",
        ),
    ]
