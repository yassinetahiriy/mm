# Generated by Django 5.0.6 on 2025-01-02 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APPELEARNING", "0005_matiere1bac"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cours",
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
                ("contenu", models.TextField()),
                ("date_ajout", models.DateTimeField(auto_now_add=True)),
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
    ]
