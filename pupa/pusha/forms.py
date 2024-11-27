from django import forms
from .models import ImageFeed
from django import forms
# from .forms import  AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ImageUpload

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Обязательное поле. Введите действительный адрес электронной почты.')

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class ImageFeedForm(forms.ModelForm):
    class Meta:
        model = ImageFeed
        fields = ['image']





class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']

class UploadImageForm(forms.Form):
    image = forms.ImageField(label='Select an image')