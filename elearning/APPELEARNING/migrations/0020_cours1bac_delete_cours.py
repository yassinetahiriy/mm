# Generated by Django 5.0.6 on 2025-01-07 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APPELEARNING", "0019_niveau"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cours1Bac",
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
                ("description", models.TextField(blank=True, null=True)),
                ("video", models.FileField(blank=True, null=True, upload_to="videos/")),
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
