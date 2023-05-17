from django.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Notes

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'note']

        widgets = {
            'title' : TextInput(attrs={
                        'class' : 'form-control form-inputs',
                        'placeholder' : 'Title',
                        }),
            'note'  : Textarea(attrs={
                        'class' : 'form-control form-inputs',
                        'placeholder' :'Note',
                        'rows' : '5',
                        'cols' : '5'
                        })
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        note = super().save(commit=False)
        note.user = self.request.user
        if commit:
            note.save()
        
        return note
        

class CreateUserForm(UserCreationForm):
    email = EmailField(widget=EmailInput(attrs={'class' : 'form-control form-inputs',
                                                'placeholder' : 'Email', 
                                                'id' : 'email', 
                                                'name' : 'email',
                                                'autocomplete' : 'off'}))
    password1 = CharField(widget=PasswordInput(attrs={'class' : 'form-control form-inputs',
                                                    'placeholder' : 'Password', 
                                                    'id' : 'password', 
                                                    'name' : 'password',
                                                    'autocomplete' : 'off'}))
    password2 = CharField(widget=PasswordInput(attrs={'class' : 'form-control form-inputs',
                                                    'placeholder' : 'Confirm Password', 
                                                    'id' : 'password2', 
                                                    'name' : 'password',
                                                    'autocomplete' : 'off'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username' : TextInput(attrs={'class' : 'form-control form-inputs',
                                          'placeholder' : 'Username', 
                                          'id' : 'username', 
                                          'name' : 'username',
                                          'autocomplete' : 'off'}),
        }