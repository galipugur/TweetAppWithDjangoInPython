from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

# django formlarında html i kendisi otomatik oluşturacak. html de yazdığımız forma benzer olarak djangonun kendi formu var.

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname", max_length=50)
    message_input = forms.CharField(label="Message", max_length=100, widget=forms.Textarea(attrs={"class":"tweetmessage"}))

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username", "message"]