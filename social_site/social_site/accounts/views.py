from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    ## ^ setting this attribute equal to the form
    ##  'UserCreateForm' in forms.py (not calling it)
    success_url = reverse_lazy('login')
    # ^ Once submit has been hit on signup, back to home
    template_name = 'accounts/signup.html'
