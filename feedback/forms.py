from django import forms

class LoginForm(forms.Form):
	username=forms.CharField(label='Login', max_length=100)
	password=forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
	
class MsgForm(forms.Form):
	#date=forms.DateTimeField(disabled=True)
	email=forms.EmailField(label='E-mail', max_length=100)
	text=forms.CharField(label='Message', max_length=1000, widget=forms.Textarea)