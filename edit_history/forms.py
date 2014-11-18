from django.forms import ModelForm
from django.forms import TextInput
from edit_history.models import Url

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['title']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter wikipedia url'})}

