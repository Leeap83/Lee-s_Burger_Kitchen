from django import forms
from .models import Product, Ingredients

ingredients = forms.ModelChoiceField(
    queryset=Ingredients.objects,
    empty_label=None, widget=forms.CheckboxSelectMultiple)


class CustomForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('ingredients', 'custom_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredients'].widget.attrs['autofocus'] = True
