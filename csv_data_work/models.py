from django.contrib.auth import get_user_model
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
