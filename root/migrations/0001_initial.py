# Generated by Django 5.1.4 on 2025-01-12 02:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Admin", "Admin"),
                            ("Moderator", "Moderator"),
                            ("Verifiziert", "Verifiziert"),
                            ("Standard", "Standard"),
                        ],
                        max_length=50,
                        verbose_name="Rolle",
                    ),
                ),
                ("priority", models.IntegerField(verbose_name="Stufe")),
            ],
        ),
        migrations.CreateModel(
            name="DetailUser",
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
                (
                    "biography",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="Biografie"
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("male", "Männlich"),
                            ("female", "Weiblich"),
                            ("divers", "Divers"),
                        ],
                        max_length=50,
                        verbose_name="Geschlecht",
                    ),
                ),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="Geburtstag"),
                ),
                (
                    "profession",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Tätigkeit"
                    ),
                ),
                (
                    "place_of_residence",
                    models.CharField(max_length=100, verbose_name="Wohnort"),
                ),
                (
                    "place_of_origin",
                    models.CharField(max_length=100, verbose_name="Heimatort"),
                ),
                (
                    "relationship",
                    models.CharField(
                        choices=[
                            ("single", "Single"),
                            ("getting_to_know", "Kennenlernphase"),
                            ("in_relationship", "In einer Beziehung"),
                            ("engaged", "Verlobt"),
                            ("married", "Verheiratet"),
                            ("complicated", "Es ist kompliziert"),
                            ("separated", "Getrennt"),
                            ("divorced", "Geschieden"),
                            ("widowed", "Verwitwet"),
                            ("other", "Sonstiges"),
                        ],
                        max_length=50,
                        verbose_name="Beziehungsstatus",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LegalUser",
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
                (
                    "privacy",
                    models.BooleanField(
                        default=False, verbose_name="Datenschutzerklärung"
                    ),
                ),
                (
                    "disclaimer",
                    models.BooleanField(
                        default=False, verbose_name="Haftungsausschluss"
                    ),
                ),
                (
                    "terms",
                    models.BooleanField(
                        default=False, verbose_name="Nutzungsrichtlinien"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Nickname",
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
                ("nickname", models.CharField(max_length=100, verbose_name="Nickname")),
                (
                    "nicknamed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nicknamer",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer, der einen Nickname erhält",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nicknamed",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer, der Nicknames vergibt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConfigUser",
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
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="config",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="root.role",
                        verbose_name="Rolle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialUser",
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
                (
                    "blocked",
                    models.ManyToManyField(
                        blank=True,
                        related_name="blocked",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Blockiert",
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True,
                        related_name="friends_with",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Freunde",
                    ),
                ),
                (
                    "received_requests",
                    models.ManyToManyField(
                        blank=True,
                        related_name="received_friend_requests",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Erhaltene Anfragen",
                    ),
                ),
                (
                    "sent_requests",
                    models.ManyToManyField(
                        blank=True,
                        related_name="sent_friend_requests",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Gesendete Anfragen",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Benutzer",
                    ),
                ),
            ],
        ),
    ]
