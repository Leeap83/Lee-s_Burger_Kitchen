from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Ingredients, Category, Custom_burger


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-0'


class CustomForm(forms.ModelForm):
    custom_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-text'}), required=False)
    ingredients = forms.ModelChoiceField(
        queryset=Ingredients.objects, empty_label=None,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Custom_burger
        fields = (
            'custom_name',
            'ingredients',
        )
