# Generated by Django 5.0.6 on 2025-01-02 23:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APPELEARNING", "0006_cours"),
    ]

    operations = [
        migrations.AddField(
            model_name="matiere1bac",
            name="cours",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="Cours",
        ),
    ]
