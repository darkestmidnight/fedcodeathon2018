from django import forms
from django.contrib.auth.models import User
from .models import Profile, Alerts

class UpdateUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email',)

# form for the extension of User model
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('emergency_contact', 'office_location', 'phone_number')

class AlertsForm(forms.ModelForm):
    class Meta:
        model = Alerts
        fields = ('title', 'description',)

