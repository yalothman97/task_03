from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    "my_list": [
    {"restaurant_name":"elevation", "food_type":"burger"},
    {"restaurant_name":"roots", "food_type":"rice"},
    {"restaurant_name":"mcdonalds", "food_type":"mcchicken",},
    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {
    "restaurant_name":"almakan", "food_type":"karagi"
    }

    }
    return render(request, 'detail.html', context)
