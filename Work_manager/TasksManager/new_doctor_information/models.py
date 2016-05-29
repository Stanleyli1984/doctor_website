from django.db import models
from django import forms

class NewRegistrationModel(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(
                                max_length=50
                                )
    #password2 = forms.CharField(
    #                            label=u'Password (Again)',
    #                            widget=forms.PasswordInput()
    #                            )

    def __str__(self):
        return self.username

class NewRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = NewRegistrationModel
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

