from django import forms
from .models import UpdateUserInfo

class UpdateUserInfoForm(forms.ModelForm):

    class Meta:
        model = UpdateUserInfo
        fields = ('new_email',)