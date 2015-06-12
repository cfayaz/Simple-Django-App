from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model  = SignUp
        fields = ['full_name','email']
        # exclued = ['full_name']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'edu' in email:
            raise forms.ValidationError("Please use a valid edu email")
        return email