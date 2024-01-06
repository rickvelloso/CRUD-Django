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

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios') 
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario_id': usuario_id})
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
