from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Schema(models.Model):
    SEPARATORS = [
        (",", "Comma(,)"),
        (";", "Semicolon(;)"),
        ("\t", "Tab(\\t)"),
        (" ", "Space( )"),
        ("|", "Pipe(|)"),
    ]

    CHARACTERS = [
        ('"', 'Double-quote(")'),
        ("'", "Single-quote(')"),
    ]
    name = models.CharField(
        max_length=255, blank=True, null=True, default="New Schema"
    )
    column_separator = models.CharField(
        choices=SEPARATORS, default=",", max_length=1
    )
    string_character = models.CharField(
        choices=CHARACTERS, default='"', max_length=1
    )
    modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="schemas"
    )

    def __str__(self):
        return self.name


class Column(models.Model):
    TYPES = [
        ("Full name", "Full name (a combination of first name and last name)"),
        ("Job", "Job"),
        ("Email", "Email"),
        ("Domain name", "Domain name"),
        ("Phone number", "Phone number"),
        ("Company name", "Company name"),
    ]

    column_name = models.CharField(max_length=255)
    type = models.CharField(choices=TYPES, max_length=255)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.column_name} ({self.type})"
