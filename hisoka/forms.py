# coding=utf-8
from django import forms

from hisoka.models import Fireball, FeralSpirit, CartaMagicPy
from hisoka.magic_images import rakatica


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


class FormNuevaCarta(forms.ModelForm):

    imagen = forms.URLField(help_text="URL pegada de http://www.smfcorp.net",
                            widget=forms.URLInput(attrs={'class': 'form-control'}))
    grupo = forms.CharField(help_text="Librería / Subtema",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CartaMagicPy
        fields = ['grupo', 'nombre', 'descripcion']

        widgets = {
            'grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }

    def save(self, **kwargs):

        url_imagen = self.cleaned_data['imagen']
        imagen_recortada = rakatica(url_imagen)
        self.imagen = imagen_recortada

        return super(FormNuevaCarta, self).save(commit=True)
