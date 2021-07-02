from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    For the front end to calculate the price
    """
    return price * quantity
