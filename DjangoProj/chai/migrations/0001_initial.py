# Generated by Django 5.0.6 on 2024-06-19 19:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="chaiVariety",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images/")),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("ML", "Masala"),
                            ("GC", "Ginger"),
                            ("CC", "Cardamom"),
                            ("KC", "Kashmiri"),
                        ],
                        default="ML",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]