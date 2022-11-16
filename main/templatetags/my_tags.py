from django import template


register = template.Library()


@register.simple_tag
def mobile():
    return 'mobile'

@register.simple_tag
def computers():
    return 'computers'

@register.simple_tag
def laptops():
    return 'laptops'

@register.simple_tag
def tv_video():
    return 'tv/video'

@register.simple_tag
def home_tech():
    return 'home_tech'

@register.simple_tag
def children():
    return 'children'

@register.simple_tag
def audio():
    return 'audio'
