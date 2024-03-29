from .models import Response
from django.forms import ModelForm, RadioSelect


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['question1', 'question2']  # add more fields as needed
        widgets = {
            'question1': RadioSelect(choices=Response.QUESTION1_CHOICES, attrs={'class': 'form-check-input'}),
            'question2': RadioSelect(choices=Response.QUESTION2_CHOICES, attrs={'class': 'form-check-input'}),

        }

