from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormLinks
from .models import Link


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'index.html', {'form': form, 'status': status})

def loading_screen(request, linkKey):
    """
    Renderiza a página de loading e passa o linkKey como contexto.
    """
    return render(request, 'animation.html', {'linkKey': linkKey})

def valida_link(request):
    """
    Valida e salva o link, redireciona para a página de loading após salvar.
    """
    form = FormLinks(request.POST)

    linkKey = form.data.get('linkKey')

    # Verifica se o link já existe
    link = Link.objects.filter(linkKey=linkKey)

    if len(link) > 0:
        return redirect("/?status=1")

    if form.is_valid():
        try:
            form.save()
            # Após salvar, redireciona para a tela de loading
            return redirect(f'/loading/{linkKey}/')
        except:
            return redirect("/?status=2")
    return redirect('/')

def success_page(request, linkKey):
    """
    Renderiza a página de sucesso com as informações do link.
    """
    return render(request, 'success.html', {'linkKey': linkKey})

def redirecionar(request, link):

    links = Link.objects.filter(linkKey = link)

    if len(links) == 0:
        return redirect('/')
    print(links)
    return redirect(links[0].linkOriginal)