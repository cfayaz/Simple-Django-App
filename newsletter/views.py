from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def home(request):
    title = 'Understanding Context'
    if request.user.is_authenticated():
        welcome = 'Welcome '+str(request.user)
    else:
        welcome = 'Welcome Guest'
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        # instance.email
        # instance.full_name
        instance.save()
    context = {
        "template_title":title,
        "welcome":welcome,
        "form":form,
    }
    return render(request, "home.html", context)