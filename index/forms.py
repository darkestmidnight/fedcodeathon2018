from django import forms
from django.contrib.auth.models import User

class UpdateUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email',)