from django.shortcuts import render
from shop.models import Item
def item_list(request):
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
    })