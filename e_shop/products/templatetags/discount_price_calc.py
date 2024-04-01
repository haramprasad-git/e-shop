from django import template

register = template.Library()

@register.filter(name='discount_price_calc')
def discount_price_calc(product):
    mrp = product.mrp
    discount_percent = product.discount_percent
    return mrp * ((100-discount_percent) / 100)