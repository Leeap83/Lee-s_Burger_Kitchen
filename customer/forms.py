from django import forms
from customer.models import Review, RATING_CHOICES


class RatingForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-text'}), required=False)
    rate = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect(
            attrs={'class': 'form-check-inline'}), required=True)
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-text'}), required=False)

    class Meta:
        model = Review
        fields = (
            'title',
            'rate',
            'comment',
        )
