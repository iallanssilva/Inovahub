from django import forms


class Contact(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form_name',
                                      'title': 'Digite o seu Nome',
                                      'placeholder': 'Clique e inclua o seu nome'})
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=256,
        widget=forms.EmailInput(attrs={'class': 'form_email',
                                       'title': 'Digite o seu Nome',
                                       'placeholder': 'Clique e inclua o seu e-mail'})
    )
    mensagem = forms.CharField(
        label='Mensagem',
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form_message',
                                     'title': 'Digite a sua Mensagem',
                                     'placeholder': 'Clique e nos conte como podemos te ajudar'})
    )
