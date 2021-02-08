from django import forms
from django.contrib.auth.models import User


class Signup_Form(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	confirm_password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'confirm_password'
			]



class Login_Form(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
		