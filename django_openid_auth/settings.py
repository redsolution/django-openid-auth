from django.conf import settings

DEFAULT_OPENID_PROVIDERS = [
        {'name':'yandex', 'url':'http://openid.yandex.ru/',
            'img': '/media/django_openid_auth/img/openid_logos/yandex.png'},
        {'name':'google', 'url': 'https://www.google.com/accounts/o8/id',
            'img': '/media/django_openid_auth/img/openid_logos/google.png'},
    ]

OPENID_PROVIDERS = getattr(settings, 'OPENID_PROVIDERS',
                             DEFAULT_OPENID_PROVIDERS)
