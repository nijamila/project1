from django import forms
from .models import SupportMessage

class SupportMessageForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':4, 'placeholder':'Type your message here...'})
        }

