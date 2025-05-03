from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Senha')
    remember_token = forms.CharField(widget=forms.HiddenInput(), required=False) # Campo para o remember token, oculto no cadastro

    class Meta:
        model = Cliente
        fields = ['full_name', 'user_name', 'tel', 'email', 'password', 'remember_token']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Escolha um nome de usuário único'}),
            'tel': forms.TextInput(attrs={'placeholder': 'Ex: (11) 99999-9999'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com'}),
            # O widget para password e confirm_password já está definido acima
        }
        labels = {
            'full_name': 'Nome Completo',
            'user_name': 'Nome de Usuário',
            'tel': 'Telefone (Celular)',
            'email': 'Email',
            'password': 'Senha',
            'remember_token': '', # Sem label para o campo oculto
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Não vamos exibir o remember_token no formulário de cadastro
        del self.fields['remember_token']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user