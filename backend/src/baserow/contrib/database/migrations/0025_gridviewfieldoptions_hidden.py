# Generated by Django 2.2.11 on 2020-11-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0024_selectoption_singleselectfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="gridviewfieldoptions",
            name="hidden",
            field=models.BooleanField(default=False),
        ),
    ]
