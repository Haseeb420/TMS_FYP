import email
import re
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True, max_length=50,
                             error_messages={
                                 "required": "Email must not be Empty.",
                                 "max_length": "Please enter a shorter email"})
    password = forms.CharField(
        label='Password', required=True, widget=forms.PasswordInput)
