from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','sex','school','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'例如：李德新'}),
                    'sex': forms.RadioSelect(),
                    'school': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
