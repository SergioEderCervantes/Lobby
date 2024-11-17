from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('AD', 'Admin'),
        ('US', 'User'),
        ('GU', 'Guest'),
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
        default="US",
    )

    email = models.EmailField(
        _("Correo electrónico"),
        blank=False,
        unique=True,
        error_messages={
            "unique": _("Ya existe un usuario con este correo electrónico, por favor verifíquelo."),
        },
    )
    
    # Eliminar Groups, ya que por la naturaleza del proyecto no seran necesarios
    groups = None
    
    # Proper config for user permissions
    user_permissions = models.ManyToManyField(
    Permission,
    related_name="customuser_permissions",  # Nombre único
    blank=True,
    )
    def save(self, **kwargs):
        # Ajustes previos a guardar para mantener la coherencia en la base de datos
        if self.tipo_usuario == 'AD':
            self.is_staff = True
            self.is_superuser = True
        if self.is_staff or self.is_superuser:
            self.tipo_usuario = 'AD'
        super().save(**kwargs)

