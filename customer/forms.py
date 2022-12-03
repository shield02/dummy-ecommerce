from django import forms
from customer.models import Customer

class SignInForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("email","password",)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("email","firstname","lastname","password")

class ForgotPasswordForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("email",)

