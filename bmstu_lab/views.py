from django.shortcuts import render
from datetime import date

def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def MainPage(request):
    return render(request, 'index.html', {'data': {
        'cards': [{
            'title': 'Обработка помещений после ковида',
            'desc': 'Дэзинфекция объектов',
            'cost': '50 500',
            'img': './img/1.png',
            'id': 1
        }]
    }})

def sendText(request):
    input_text = request.POST['text']

def CustomPage(request, id):
    return render(request, 'page.html', {'data':{
        'id': id
    }})

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Книга с картинками', 'id': 1},
            {'title': 'Бутылка с водой', 'id': 2},
            {'title': 'Коврик для мышки', 'id': 3},
        ]
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})
