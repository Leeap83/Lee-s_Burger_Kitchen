from django import forms
from customer.models import Review, RATING_CHOICES


class RatingForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-text'}), required=False)
    rate = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Review
        fields = ('comment', 'rate', 'user')
