from django import template

register = template.Library()

@register.filter(name='discount_price_calc')
def discount_price_calc(mrp, discount_percent):
    return mrp * ((100-discount_percent) / 100)