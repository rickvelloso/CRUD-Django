from django import forms
from .models import Usuario
from validate_docbr import CPF

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'senha', 'email', 'cpf', 'data_nascimento', 'foto']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf_validator = CPF()

        if not cpf_validator.validate(cpf):
            raise forms.ValidationError('CPF inválido. Por favor, insira um CPF válido.')

        return cpf
