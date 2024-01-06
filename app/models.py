from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF
import uuid
def upload_image_formater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to="img/%y")

    def clean(self):
        cpf_validator = CPF()

        if not cpf_validator.validate(self.cpf):
            raise ValidationError({'cpf': 'CPF inválido. Por favor, insira um CPF válido.'})


# Adicione esta linha abaixo do bloco da classe Usuario
class Meta:
    app_label = 'app'

