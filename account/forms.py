from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django import forms
from account.models import UserProfile
User = get_user_model()

class UserLoginForm(forms.ModelForm):
    password   = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        model = User
        fields = [
            'username',
            'password',
        ]

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                    raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                    raise forms.ValidationError("incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user no longer active")

        return super(UserLoginForm,self).clean()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('photo','bio','country')


class UserRegistrationForm(forms.ModelForm):
    firstname           = forms.CharField(max_length=20)
    lastname            = forms.CharField(max_length=20)
    email               = forms.EmailField()
    email2              = forms.EmailField()
    password            = forms.CharField(widget=forms.PasswordInput,max_length=20 )
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=20)



    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'email',
            'email2',
            'password',
            'password2',

        ]
    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        password    = self.cleaned_data.get('password')
        passwors2   = self.cleaned_data.get('password2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        if password != passwors2:
            raise forms.ValidationError("Passwords must much")
        return super(UserRegistrationForm,self).clean()






