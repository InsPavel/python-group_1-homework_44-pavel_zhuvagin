from django import template

register = template.Library()

@register.inclusion_tag('order_list.html')
def order_food_pk(pk):
    return {'pk': pk}