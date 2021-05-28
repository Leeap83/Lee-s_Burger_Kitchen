from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Custom_burger
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
            'ingredients',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('custom_name'),
            ),
            InlineCheckboxes('ingredients'),
            FormActions(
                Submit(
                    'create_burger',
                    'Create Burger',
                    css_class='btn btn-secondary')
            )
        )
