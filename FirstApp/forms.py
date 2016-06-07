from django import forms
from .models import Entry, Blogger, Blog
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


class PostForm(forms.ModelForm):

    class Meta:
        model = Entry
        #exclude = ['author', 'pub_date']
        fields = ('headline', 'body_text',)
