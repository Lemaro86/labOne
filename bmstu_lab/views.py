from django.shortcuts import render
from bmstu_lab.models import Service


def main_page(request):
    card_items = Service.objects.all()
    print(card_items)
    return render(request, 'index.html', {'data': {
        'cards': card_items,
        'search': ''
    }})


def send_text(request):
    input_text = request.POST['text']
    search_by_title = Service.objects.filter(title__contains=input_text)
    search_by_cost = Service.objects.filter(cost__contains=input_text)
    union_all = search_by_title.union(search_by_cost)
    return render(request, 'index.html', {'data': {
        'cards': union_all,
        'search': input_text
    }})


def custom_page(request, id):
    card_item = Service.objects.get(pk=id)
    return render(request, 'page.html', {'data': card_item})


def orders_page(request):
    return render(request, 'orders.html')

