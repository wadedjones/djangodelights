# Generated by Django 4.1.4 on 2022-12-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_alter_ingredients_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchases",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
