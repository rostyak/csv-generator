# Generated by Django 4.1.4 on 2022-12-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csv_data_work", "0003_alter_schema_column_separator"),
    ]

    operations = [
        migrations.CreateModel(
            name="Column",
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
                ("column_name", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            (
                                "Full name",
                                "Full name (a combination of first name and last name)",
                            ),
                            ("Job", "Job"),
                            ("Email", "Email"),
                            ("Domain name", "Domain name"),
                            ("Phone number", "Phone number"),
                            ("Company name", "Company name"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
            ],
        ),
    ]
