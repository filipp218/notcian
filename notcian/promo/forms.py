from django.forms import ModelForm
from promo.models import Advert
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        exclude = ['url', 'author']

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class AuthProfileForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
