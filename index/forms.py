from django import forms
from django.contrib.auth.models import User
from .models import Profile, Alerts

# form to update user info (email)
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

# form to fill up to create an alert
class AlertsForm(forms.ModelForm):
    class Meta:
        model = Alerts
        fields = ('title', 'description',)

