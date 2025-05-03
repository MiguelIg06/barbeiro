from django.db import models
from django.contrib.auth.hashers import make_password

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)  # Django cria um id automático por padrão, mas podemos explicitá-lo
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    tel = models.CharField(max_length=11, blank=True, null=False)  # comprimento max_length
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=128, verbose_name='Senha') # Novo campo para a senha criptografada
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name # Retorna o nome completo do cliente
    
    def save(self, *args, **kwargs):
         # Sobrescreve o método save para criptografar a senha antes de salvar
        if not self.password.startswith('pbkdf2_sha256$'): # Verifica se a senha já não está criptografada
            self.password = make_password(self.password) # Criptografa a senha usando a função do Django
        super().save(*args, **kwargs) # Chama o método save da classe pai (forms.ModelForm) para salvar o objeto no banco de dados
