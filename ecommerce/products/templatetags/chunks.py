from django import template
register=template.Library()
@register.filter(name='chunks')
def chunks(lst,chunk_size): 