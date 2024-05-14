from django.shortcuts import render
from bmstu_lab.models import Cards


def main_page(request):
    card_items = Cards.objects.all()
    return render(request, 'index.html', {'data': {
        'cards': card_items,
        'search': ''
    }})


def send_text(request):
    input_text = request.POST['text']
    filtered_data = Cards.objects.filter(title__contains=input_text)
    print(input_text)
    print(filtered_data)
    return render(request, 'index.html', {'data': {
        'cards': filtered_data,
        'search': input_text
    }})


def custom_page(request, id):
    card_item = Cards.objects.get(pk=id)
    return render(request, 'page.html', {'data': card_item})


def orders_page(request):
    return render(request, 'orders.html')
