from django.shortcuts import render
from .models import MenuItem 
from .models import *
from django.db.models import Q
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    query = request.GET.get('q')
    category_slug = request.GET.get('category')  # this is now the choice value

    items = MenuItem.objects.filter(is_available=True)

    # Filter by category (directly use the value from choices)
    if category_slug:
        items = items.filter(category=category_slug)

    # Filter by search query
    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # If you want to show all possible categories (from choices)
    categories = [choice[0] for choice in MenuItem._meta.get_field('category').choices]

    context = {
        'items': items,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    }
    return render(request, 'menu/menu.html', context)

def add_to_cart(request):
    item_id = request.POST.get('item_id')
    quantity = int(request.POST.get('quantity', 1))

    if item_id:
        try:
            item = MenuItem.objects.get(id=item_id)
            cart = request.session.get('cart', {})

            if item_id in cart:
                cart[item_id]['quantity'] += quantity
            else:
                cart[item_id] = {
                    'name': item.name,
                    'price': str(item.price),
                    'quantity': quantity,
                    'image': item.image_url
                }
            
            request.session['cart'] = cart
            return JsonResponse({'status': 'success', 'cart': cart})
        except MenuItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def remove_from_cart(request):
    item_id = request.POST.get('item_id')
    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]
        request.session['cart'] = cart
        return JsonResponse({'status': 'success', 'cart': cart})
    
    return JsonResponse({'status': 'error', 'message': 'Item not in cart'})

def update_cart(request):
    item_id = request.POST.get('item_id')
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if item_id in cart:
        if quantity > 0:
            cart[item_id]['quantity'] = quantity
        else:
            del cart[item_id]
        
        request.session['cart'] = cart
        return JsonResponse({'status': 'success', 'cart': cart})
    
    return JsonResponse({'status': 'error', 'message': 'Item not in cart'})

def place_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not cart:
            return JsonResponse({'status': 'error', 'message': 'Cart is empty'})

        # You might want to associate the order with a user or table
        # For now, let's create a simple order
        order = Order.objects.create(status='pending')

        for item_id, item_data in cart.items():
            try:
                menu_item = MenuItem.objects.get(id=item_id)
                OrderItem.objects.create(
                    order=order,
                    item=menu_item,
                    quantity=item_data['quantity']
                )
            except MenuItem.DoesNotExist:
                # Handle case where a menu item in the cart doesn't exist anymore
                # You might want to log this or return an error
                pass
        
        # Clear the cart
        request.session['cart'] = {}

        return JsonResponse({'status': 'success', 'message': 'Order placed successfully!'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

