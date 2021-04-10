from django import forms
from .models import Og_Img, Background

class ImgForm(forms.ModelForm):
    class Meta:
        model = Og_Img
        fields = ['img']
       #S widgets = {'img': forms.HiddenInput()}

    
class BgForm(forms.ModelForm):
    class Meta:
        model = Background
        fields = ('bg_img',)
