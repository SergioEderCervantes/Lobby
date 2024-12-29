from django.shortcuts import render
from allauth.account.forms import SignupForm


class custom_signup(SignupForm):
    def save(self, request):
        user = super(custom_signup, self).save(request)
        user.telefono = self.cleaned_data['telefono']
        user.save()
        return user
    
