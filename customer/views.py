from django.shortcuts import render, redirect
from django.http import HttpResponse
from customer.forms import SignInForm, SignUpForm, ForgotPasswordForm
from customer.models import Customer

# Create your views here.
def index(request):
    return render(
        request,
        'customer/index.html'
    )

def sign_in(request):
    form = SignInForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = hash(form.cleaned_data.get('password'))

            return redirect('home')
    else:
        return render(
            request,
            'customer/auth/sign-in.html', 
            {
                'message': "Sign in was successful.",
            }
        )

def sign_up(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            password = hash(form.cleaned_data.get('password'))

            customer = Customer(email=email, firstname=firstname, lastname=lastname, password=password)
            customer.save()

            return redirect('home')
    else:
        return render(
            request,
            'customer/auth/sign-up.html'
        )

def forgot_password(request):
    return render(
        request,
        'customer/auth/forgot-password.html'
    )
