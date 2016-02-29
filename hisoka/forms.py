
from django import forms

from hisoka.models import Fireball, FeralSpirit


class FormCrearFireball(forms.ModelForm):

    class Meta:
        model = Fireball
        fields = ['nombre', 'url_amazon', 'twitter', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'url_amazon': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'})
        }


class FormCrearFeralSpirit(forms.ModelForm):

    class Meta:
        model = FeralSpirit
        fields = ['tipo', 'nombre', 'url']

        _tipos_feral = (
            ('video', 'Video'),
            ('imagen', 'Imagen'),
            ('texto', 'Texto')
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=_tipos_feral, attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }
