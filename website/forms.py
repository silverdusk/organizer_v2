from django import forms
from .models import MyModel


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['Name', 'Date', 'IsActive', 'Description']
    # name = forms.CharField(max_length=50)
    # date = forms.DateField(input_formats=['%d/%m/%Y'])
    # is_active = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], initial='yes')
    # description = forms.CharField(widget=forms.Textarea, max_length=300)
