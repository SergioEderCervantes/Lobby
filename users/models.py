import random
import string
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError
class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('AD', 'Admin'),
        ('US', 'User'),
        ('GU', 'Guest'),
    ]
    
    tipo_usuario = models.CharField(
        _("Tipo de usuario"),
        blank=False,
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default="US",
    )

    email = models.EmailField(
        _("Correo electrónico"),
        # TODO: settear False si se quiere obligar a poner email
        blank=False,
        # TODO: Settear a True, este si es de ahuevo pero lo puse False para hacer pruebas
        unique=True,
        error_messages={
            "unique": _("Ya existe un usuario con este correo electrónico, por favor verifíquelo."),
        },
    )
    
    telefono = models.CharField(
        _("Numero de telefono"),        
        max_length=15,
        null=False, 
        blank=False,
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',  
        null=True,
        blank=True,
        verbose_name="Avatar del usuario"
    )
    # Eliminar Groups, ya que por la naturaleza del proyecto no seran necesarios
    groups = None
    
    # Proper config for user permissions
    user_permissions = models.ManyToManyField(
    Permission,
    related_name="customuser_permissions",  # Nombre único
    blank=True,
    )
    
    juegos_inscritos = models.JSONField(_("Nombres de juegos que ya se inscribio"), default=list)
    
    def generar_numero_celular(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])
    
    def generar_correo_electronico(self):
        # Generar un nombre de usuario aleatorio de 8 caracteres
        usuario = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        # Dominio fijo o aleatorio
        dominio = 'example.com'
        return f"{usuario}@{dominio}"
    
    def save(self, **kwargs):
        # Ajustes previos a guardar para mantener la coherencia en la base de datos        
        if self.tipo_usuario == 'AD':
            self.is_staff = True
            self.is_superuser = True
        if self.is_staff or self.is_superuser:
            self.tipo_usuario = 'AD'
            
        # Ajustes para asegurarse que el superuser tenga numero y los guest tengan correo
        if self.is_superuser and not self.telefono:
            while True:
                aux = self.generar_numero_celular()
                # Validar unicidad
                if not User.objects.filter(telefono = aux).exists():
                    self.telefono = aux
                    break
        elif self.tipo_usuario == 'GU' and not self.email:
            while True:
                aux = self.generar_correo_electronico()
                # Validar unicidad
                if not User.objects.filter(email = aux).exists():
                    self.email = aux
                    break
        
        
        
        super().save(**kwargs)

    def agregar_juego(self, nombre_juego: str) -> bool:
        """
        Agrega un juego a la lista de juegos inscritos si no está ya inscrito.
        Aplica una promoción si alcanza el límite de 6 juegos inscritos.
        
        :param nombre_juego: Nombre del juego a agregar.
        :return: True si se aplica la promoción y se reinicia la lista, False si no.
        """
        if not isinstance(nombre_juego, str):
            raise ValueError("El nombre del juego debe ser un string.")

        # Verificar si el juego ya está en la lista
        if nombre_juego not in self.juegos_inscritos:
            self.juegos_inscritos.append(nombre_juego)
            
            # Verificar si se alcanza el límite para la promoción
            if self.num_torneos_dif_inscritos() >= 6:
                self.juegos_inscritos.clear()  # Reiniciar la lista de juegos inscritos
                self.save()  # Guardar el cambio después de reiniciar
                return True

            self.save()  # Guardar el cambio después de agregar el juego
        
        return False

    def num_torneos_dif_inscritos(self) -> int:
        return len(self.juegos_inscritos)