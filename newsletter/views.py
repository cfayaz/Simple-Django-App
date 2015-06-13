from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import SignUpForm,ContactForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    title = 'Understanding Context'
    if request.user.is_authenticated():
        welcome = 'Welcome '+str(request.user)
    else:
        welcome = 'Welcome Guest'
    form = SignUpForm(request.POST or None)
    context = {
        "template_title":title,
        "welcome":welcome,
        "form":form,
    }
    if form.is_valid():
        instance = form.save(commit = False)
        # instance.email
        # instance.full_name
        instance.save()
        welcome = 'Thanks '+instance.full_name
        context = {
            "template_title":title,
            "welcome":welcome,
            "form":form,
        }
        return HttpResponseRedirect('')


    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print str(form)
        for k,val in form.cleaned_data.iteritems():
            print k,val
        form_email=form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        subject = 'contact site test'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['cfayaz@gmail.com']
        contact_message= "%s says %s via %s"%(form_full_name,form_message,form_email)
        send_mail(subject,
            contact_message,
            from_email,
            to_email,
            fail_silently = False)
    context={
        "form":form,
        "title":"Contact Form"
    }
    return render(request,"contact.html",context)