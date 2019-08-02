from django import forms
from .models import Messages

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email= forms.EmailField(required=False)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class MessagesForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ('name', 'email', 'subject', 'message')
