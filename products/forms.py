from django import forms
from .models import Product, Ingredients, Category

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


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-0'
