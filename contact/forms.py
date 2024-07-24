from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(                     # se isto form comentado ele usara o que esta no models.py
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category')


    def clean(self):                                       # ideal para validação de mais de um valor.
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Segundo nome não pode ser igual ao primeiro',
                code='invalid'
            )
            self.add_error('last_name', msg)
        
        return super().clean()
    

    def clean_first_name(self):                             # ideal para validação de apenas um valor.
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error('first_name', ValidationError(
                'Não digite "ABC" neste campo.', 
                code='invalid'
            )
        )

        return first_name
