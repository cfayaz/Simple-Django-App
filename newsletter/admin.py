from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","creation_date","updated_on"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp,SignUpAdmin)
