from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Config, Remark


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = ContactForm
        context["remarks"] = Remark.objects.all()[:5]
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = Config.objects.first()
        context['config'] = config
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'
    extra_context = {
        "form": ContactForm(),
    }


class ServicesPageView(TemplateView):
    template_name = 'services.html'


class ContactFormSubmitView(View):
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        config = Config.objects.first()
        if form.is_valid():
            text = f"""Dear {config.author},
            a person named {form.cleaned_data['full_name']} has submitted contact us form in nashtaconstruction.com 
            with email {form.cleaned_data["email"]}.
            his/her phone number is {form.cleaned_data['phone_number']},
            and also he/she left this message for you: \n`{form.cleaned_data['message']}`"""
            send_mail('Nashta Construction Alert!', text, 'mirfallahi2009@gmail.com',
                      recipient_list=[config.email], fail_silently=False)
            messages.success(request, 'Complete! Your message has been sent to admin.')
            return HttpResponseRedirect(reverse("home:home"))
