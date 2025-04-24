from django.db import models
from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
	name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}), required=True)
	phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=True)
	message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your Message here'}), required=False)
	# file = forms.FileField(label="", widget=forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'Upload File', 'accept': '*/*' }), required=False)

	class Meta:
		model = ContactUs
		fields = ('name', 'phone', 'email', 'message')

