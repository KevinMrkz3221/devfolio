from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

from .models import Skill, Project, Experience, Contact
from django.conf import settings
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()
        context['experiences'] = Experience.objects.all()

        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        contact.save()
        enviar_correo(contact,me=0)
        enviar_correo(contact)

        return render(request, 'home/send_email.html', {'name': contact.name})
    

def enviar_correo(context, me=1):
    subject = context.subject
    if me == 0:
        message = f'''
            Subject: Thank You for Your Message

            Dear {context.name},

            Thank you for getting in touch with me. I appreciate your interest and will be happy to assist you with whatever you need.

            I will do my best to respond to your message as soon as possible. If your inquiry is urgent, please indicate that in your message so I can prioritize accordingly.

            Thank you again for your patience and understanding.

            Best regards,
            Kevin Andres Rosales Marquez
        '''
        recipient_list = [context.email,]
    else:
        message = context.message
        message += f'''
            \n\n
            Name: {context.name}
            Email: {context.email}
            Phone: {context.phone}
        '''
        recipient_list = ['kevinarm@proton.me', 'kevin.rosales98@hotmail.com', 'kevinarm9812@gmail.com', 'kevin.rosales@mpobyte.com']
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, recipient_list)
    # Puedes redirigir o renderizar una respuesta según tus necesidades



