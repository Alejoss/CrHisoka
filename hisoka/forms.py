# coding=utf-8
import logging

from django import forms

from hisoka.models import Fireball, FeralSpirit, CartaMagicPy, GrupoMagicPy


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
        fields = ['tipo', 'texto', 'url', 'imagen']

        _tipos_feral = (
            ('video', 'Video'),
            ('imagen', 'Imagen'),
            ('texto', 'Texto')
        )

        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=_tipos_feral, attrs={'class': 'form-control', 'id': 'tipo_feral'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'id': 'imagen_input'})
        }


class MultipleImagesFeral(forms.Form):
    images = forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'})


class FormNuevaCarta(forms.ModelForm):
    queryset_grupos_magicpy = GrupoMagicPy.objects.all()
    grupo = forms.ModelChoiceField(queryset_grupos_magicpy)

    class Meta:
        model = CartaMagicPy
        fields = ['imagen', 'grupo', 'nombre', 'descripcion']
        widgets = {
            'imagen': forms.URLInput(attrs={'class': 'form-control', 'id': 'url_imagen'}),
            'grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }


class FormNuevoGrupo(forms.ModelForm):
    class Meta:
        model = GrupoMagicPy
        fields = ['nombre', 'descripcion', 'imagen']

        widgets = {
            'imagen': forms.URLInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }
