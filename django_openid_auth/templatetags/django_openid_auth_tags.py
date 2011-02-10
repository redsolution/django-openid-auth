from django import template
from django_openid_auth.settings import OPENID_PROVIDERS

register = template.Library()

@register.inclusion_tag('openid/templatetags/show_openid_providers_buttons.html',
    takes_context=True)
def show_openid_providers_buttons(context):
    u'''Show openid providers buttons'''
    return {'request':context['request'],
        'openid_providers': OPENID_PROVIDERS, }
