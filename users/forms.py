from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    phone = forms.CharField(
        max_length=15,
        required=False,
        label="Teléfono",
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono (opcional)'}),
    )

    def save(self, request):
        user = super().save(request)
        user.telefono = self.cleaned_data.get('phone', '')
        user.save()
        return user
