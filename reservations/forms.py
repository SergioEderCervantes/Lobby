from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation  # El modelo que usará el formulario
        fields = ['username', 'email', 'telefono', 'fecha', 'hora', 'num_personas', 'comentarios']
