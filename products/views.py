from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import scraping

# Create your views here.
def getViewProduct(request, page):
    pagination_number = page
    count_elements = 4
    word = ""

    if request.method == "POST":
        find_word = request.POST.get('word').lower()
        filter_word = request.POST.get('filter')
        items_count = request.POST.get('items')

        if find_word:
            word = find_word

        if items_count:
            count_elements = int(items_count)

        products_ebay = scraping.getScrapping(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={find_word.replace(' ', '+')}&_sacat=0", "ebay")
        products_mercadolibre = scraping.getScrapping(f"https://listado.mercadolibre.com.bo/{find_word.replace(' ', '-')}#D[A:componentes%20pc]", "mercado_libre")

        if filter_word == 'ebay':
            pagination_products_ebay = Paginator(products_ebay, count_elements)
            context = {'products_ebay': pagination_products_ebay.page(pagination_number), 'word': word}
            return render(request, 'products.html', context)
        
        if filter_word == 'mercado_libre':
            pagination_products_mercadolibre = Paginator(products_mercadolibre, count_elements)
            context = {'products_mercadolibre': pagination_products_mercadolibre.page(pagination_number), 'word': word}
            return render(request, 'products.html', context)

    else:
        products_ebay = scraping.getScrapping("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=productos&_sacat=0&LH_TitleDesc=0&_odkw=products&_osacat=0", "ebay")
        products_mercadolibre = scraping.getScrapping("https://listado.mercadolibre.com.bo/productos#D[A:productos]", "mercado_libre")

    pagination_products_ebay = Paginator(products_ebay, count_elements)
    pagination_products_mercadolibre = Paginator(products_mercadolibre, count_elements)

    # Carga principal
    context = {'products_mercadolibre': pagination_products_mercadolibre.page(pagination_number), 'products_ebay': pagination_products_ebay.page(pagination_number), 'word': word}
    return render(request, 'products.html', context)
