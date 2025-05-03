from django.db import models

from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)  # Django cria um id automático por padrão, mas podemos explicitá-lo
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    tel = models.CharField(max_length=11, blank=True, null=False)  # comprimento max_length
    email = models.EmailField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
