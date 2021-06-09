from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Custom_burger, Ingredients
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes, FormActions


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
    class Meta:
        model = Custom_burger
        fields = (
            'custom_name',
            # 'ingredients',
            'bun',
            'burgers',
            'sauces',
            'salad',
            'cheeses',
            'extra',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['ingredients'].queryset = Ingredients.objects.order_by('cat')
        self.fields['bun'].queryset = Ingredients.objects.filter(cat='Bun')
        self.fields['burgers'].queryset = Ingredients.objects.filter(cat='Burger')
        self.fields['sauces'].queryset = Ingredients.objects.filter(cat='Sauce')
        self.fields['salad'].queryset = Ingredients.objects.filter(cat='Salad')
        self.fields['cheeses'].queryset = Ingredients.objects.filter(cat='Cheese')
        self.fields['extra'].queryset = Ingredients.objects.filter(cat='Extras')
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('custom_name'),
            ),
            # InlineCheckboxes('ingredients'),
            InlineCheckboxes('bun'),
            InlineCheckboxes('burgers'),
            InlineCheckboxes('sauces'),
            InlineCheckboxes('salad'),
            InlineCheckboxes('cheeses'),
            InlineCheckboxes('extra'),

            FormActions(
                Submit(
                    'create_burger',
                    'Create Burger',
                    css_class='btn btn-secondary')
            )
        )
