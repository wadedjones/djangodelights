# Generated by Django 4.1.4 on 2022-12-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_reciperequirements_purchases"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredients",
            name="unit",
            field=models.CharField(max_length=50),
        ),
    ]
