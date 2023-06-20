from django import forms
from  .models import  Mueble
from django.contrib.auth.forms import UserCreationForm


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'

        widget = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    pass