from django.db import models
from django import forms
import uuid
import os

def update_filename(instance, filename):
    path = "upload/path/"
    format = str(instance.id) + os.path.splitext(filename)[1]
    return os.path.join(path, format)

class PictureModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    docfile = models.ImageField(upload_to=update_filename)

    #password2 = forms.CharField(
    #                            label=u'Password (Again)',
    #                            widget=forms.PasswordInput()
    #                            )

    def __str__(self):
        return self.name



class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureModel
        fields = ['name', 'docfile']

