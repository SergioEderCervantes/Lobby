from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('AD', 'Admin'),
        ('US', 'User'),
    ]

    username = models.CharField(
        _("Nombre de usuario"), blank=False, max_length=30, unique=True, error_messages={
            "unique": _("Ya existe un usuario con este nombre de usuario, por favor verifíquelo."),
        },
    )

    nombre = models.CharField(
        ("Nombre de usuario"), blank=False, max_length=30, default=""
    )
    
    apellido = models.CharField(
        _("Apellido de usuario"),
        blank=False,
        max_length=30,
        default="",
    )

    tipo_usuario = models.CharField(
        _("Tipo de usuario"),
        blank=False,
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default="AU",
    )

    email = models.EmailField(
        _("Correo electrónico"),
        blank=False,
        unique=True,
        error_messages={
            "unique": _("Ya existe un usuario con este correo electrónico, por favor verifíquelo."),
        },
    )

