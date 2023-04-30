from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tasks


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
                   'username',
                   'email',
                   'password1',
                   'password2'
               

        )

    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user


class CreateTask(forms.ModelForm):
 
    
    class Meta:
        
        model = Tasks
 
        
        fields = ['title','description','complete']


class UpdateTask(forms.ModelForm):
 
    
    class Meta:
        
        model = Tasks
 
        
        fields = ['title','description','complete']