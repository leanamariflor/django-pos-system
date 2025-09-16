from django import forms
from .models import YourModel   # replace with your actual model name

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'
