from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

from .models import Skill, Project, Experience, ProjectImage
from django.conf import settings

from .forms import ContactForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()
        context['experiences'] = Experience.objects.all()
        context['project_images'] = ProjectImage.objects.all()
        context['form'] = ContactForm()

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save()
                enviar_correo(contact,me=0)
                enviar_correo(contact)
                return render(request, 'home/send_email.html', {'name': contact.name})
            else:
                return render(request, 'home/home.html', {'form': form })
        else:    
            return render(request, 'home/home.html', {'form': form})
    

def enviar_correo(context, me=1):
    if me == 0:
        subject = 'Thank You for Your Message'
        message = f'''

            Dear {context.name},

            Thank you for getting in touch with me. I appreciate your interest and will be happy to assist you with whatever you need.

            I will do my best to respond to your message as soon as possible. If your inquiry is urgent, please indicate that in your message so I can prioritize accordingly.

            Thank you again for your patience and understanding.

            Best regards,
            Kevin Andres Rosales Marquez
        '''
        recipient_list = [context.email,]
    else:
        subject = context.subject
        message = context.message
        message += f'''
            \n\n
            Name: {context.name}
            Email: {context.email}
            Phone: {context.phone}
        '''
        recipient_list = ['kevinarm@proton.me', 'kevin.rosales98@hotmail.com', 'kevinarm9812@gmail.com']
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, recipient_list)



