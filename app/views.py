from django.shortcuts import render, get_object_or_404, redirect
from .forms import UsuarioForm
from .models import Usuario


def cadastrar_usuario(request):
    img = []

    if request.method == 'POST':
        form = UsuarioForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
        img = []

    return render(request, 'cadastrar_usuario.html', {"img": img, 'form': form})

def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios') 

# Sua view editar_usuario
def editar_usuario(request, usuario_id):
    # Obtém a instância do usuário que deseja editar
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        # Preenche o formulário com os dados existentes do usuário e os novos dados da requisição
        form = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        
        if form.is_valid():
            # Salva as alterações no usuário
            form.save()
            return redirect('listar_usuarios')
    else:
        # Preenche o formulário com os dados existentes do usuário
        form = UsuarioForm(instance=usuario)

    # Aqui, 'obj' será a instância do usuário que está sendo editado
    # 'img' será uma lista contendo apenas essa instância, pois você não possui uma classe de imagem separada
    obj = usuario
    img = [usuario]

    return render(request, 'editar_usuario.html', {'form': form, 'obj': obj, 'img': img, 'usuario_id': usuario.id})




def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
