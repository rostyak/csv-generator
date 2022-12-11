# Generated by Django 4.1.4 on 2022-12-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csv_data_work", "0002_alter_schema_column_separator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schema",
            name="column_separator",
            field=models.CharField(
                choices=[
                    (",", "Comma(,)"),
                    (";", "Semicolon(;)"),
                    ("\t", "Tab(\\t)"),
                    (" ", "Space( )"),
                    ("|", "Pipe(|)"),
                ],
                default=",",
                max_length=1,
            ),
        ),
    ]
