from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """
    A view to return the shopping bag
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag.
    Stores shopping basket data in a 'session'.
    Get bag variable in session or create bag object if it doesn't exist.
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # If there is a size
    # If item already in the bag, we check if item ID and same size exists
    # We then increase this if the same item and size is added, 
    # else, it equals quantity as same item new size
    # Else if no recorded item ID, just arrange according to size
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else: 
        # If there is no size
        # if item_id is one of the keys, increase quantity
        # bag's item_id key is the quantity, if there is already product key, increase quantity
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


