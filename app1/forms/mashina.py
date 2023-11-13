from django import forms

from app1.models import Auto


class Mashinaform(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
