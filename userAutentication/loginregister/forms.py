from django import forms

class LoginForm(forms.Form):
    username =forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.Form):
    password = forms.CharField(label="Password", 
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", 
                               widget=forms.PasswordInput)

