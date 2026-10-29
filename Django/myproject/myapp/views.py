from django.shortcuts import render
from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    student_id = forms.CharField(required=True)
    mobile = forms.RegexField(
        regex=r'^[6-9]\d{9}$',
        error_messages={'invalid': 'Enter valid 10-digit mobile number'}
    )
    address = forms.CharField(required=True)
    gender = forms.ChoiceField(
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )

def login(request):
    form = LoginForm(request.POST or None)
    message = ''

    if request.method == 'POST' and form.is_valid():
        message = 'Form submitted successfully!'
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'message': message
    })