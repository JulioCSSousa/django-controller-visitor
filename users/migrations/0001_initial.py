# Generated by Django 5.0.7 on 2024-08-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=194, unique=True, verbose_name="e-mail do usuário"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="usuário ativo"),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=True,
                        verbose_name="usuario da equipe de desenvolvimento",
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False, verbose_name="É um super usuário"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="custom_user_set", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="custom_user_set_permissions",
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "verbose_name": ("User",),
                "verbose_name_plural": "Users",
                "db_table": "user",
            },
        ),
    ]
