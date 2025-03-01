from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ContactForm
from .models import Subscriber

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            if form.cleaned_data.get("subscribe"):
                # Falls die E-Mail noch nicht als Abonnent existiert, wird sie angelegt
                Subscriber.objects.get_or_create(email=contact.email)
            messages.success(request, "Nachricht wurde erfolgreich gesendet!")
            return redirect("home")
        else:
            messages.error(request, "Bitte überprüfe deine Eingaben.")
    else:
        form = ContactForm()
    context = {"contact_form": form}
    return render(request, "core/home.html", context)

@staff_member_required
def send_newsletter(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')
        # Alle Abonnenten abrufen
        subscribers = Subscriber.objects.all()
        recipient_list = [s.email for s in subscribers]
        sent_count = send_mail(subject, message_body, settings.EMAIL_HOST_USER, recipient_list)
        messages.success(request, f'Newsletter gesendet an {sent_count} Empfänger.')
        return redirect('admin:index')
    return render(request, 'core/send_newsletter.html')
