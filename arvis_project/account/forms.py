from django import forms
from . import models
from django.core.validators import MaxLengthValidator,RegexValidator
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.core.validators import MaxLengthValidator, RegexValidator
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'password',)



            
class CustomUserForm(forms.ModelForm):
    username = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]{4,31}$'
            ),
            MaxLengthValidator(limit_value=30)
        ]
    )
    email = forms.EmailField()

    date_of_birth = forms.DateField()

    first_name = forms.CharField(
         validators=[MaxLengthValidator(limit_value=50)]
    )
    last_name = forms.CharField(
         validators=[MaxLengthValidator(limit_value=70)]
    )
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+77\d{9}$',
                message="Введите номер телефона в формате +7хххххххххх",
                code="invalid_phone_number",
            ),
        ]
    )

    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
 
        if password1 and password1 != password2:
            raise forms.ValidationError('Введенные пароли не совпадают')
 
    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
 
        if password1:
            user.set_password(password1)
 
        if commit:
            user.save()
 
        return user

    class Meta:
        model = CustomUser
        fields = ['username',
                  'email',
                  'date_of_birth',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'is_active',
                  'is_admin',]        