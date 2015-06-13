from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(required='False')
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'edu' in email:
            raise forms.ValidationError("Please use a.. valid edu email")
        return email

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