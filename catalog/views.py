from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

from catalog.models import Product


# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({email}): {message}')
#     return render(request, 'catalog/index.html')
def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': "Каталог продуктов"
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contact.html')


def item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': "Карточка продукта",

    }
    return render(request, 'catalog/item.html', context)

