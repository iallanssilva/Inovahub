from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from .forms import Contact
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    ano_atual = datetime.now().year
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            assunto = f'Mensagem de {nome}'
            mensagem = f'De: {nome} <{email}>\n\n{mensagem}'

            send_mail(
                assunto,
                mensagem,
                settings.EMAIL_HOST_USER,
                ['contato@inovahub.net'],
                fail_silently=False,
            )
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('/')
    else:
        form = Contact()
    return render(request, 'inovahub/pages/home.html', {'form': form, 'ano_atual': ano_atual})
