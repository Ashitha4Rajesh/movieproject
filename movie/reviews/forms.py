from django import forms
from reviews.models import Review
class reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'