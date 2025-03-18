from django.shortcuts import render
from .models import MenuItem

def home(request):
    item = MenuItem.objects.get(id=2)  # Fetch the first menu item
    return render(request, 'littleLemon/menu_card.html', {'item': item})