# Generated by Django 5.0.7 on 2024-08-04 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="visitor",
            options={"verbose_name": "Visitor", "verbose_name_plural": "Visitors"},
        ),
        migrations.RenameField(
            model_name="visitor",
            old_name="hour_authorization",
            new_name="authorization_time",
        ),
        migrations.RenameField(
            model_name="visitor",
            old_name="resident_responsible",
            new_name="authorized_by_resident",
        ),
    ]
