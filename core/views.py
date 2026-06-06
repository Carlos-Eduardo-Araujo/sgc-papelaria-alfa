from django.shortcuts import render

def login_view(request):
    return render(request, 'core/login.html')

def index_view(request):
    return render(request, 'core/index.html')

def clientes_view(request):
    return render(request, 'core/clientes.html')

def produtos_view(request):
    return render(request, 'core/produtos.html')

def vendas_view(request):
    return render(request, 'core/vendas.html')

def relatorios_view(request):
    return render(request, 'core/relatorios.html')