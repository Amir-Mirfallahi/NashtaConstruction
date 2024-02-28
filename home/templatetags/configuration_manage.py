from django import template

from ..models import Config

register = template.Library()


@register.simple_tag
def get_config(part):
    config = Config.objects.first()
    match part:
        case "address":
            return config.address
        case "phone":
            return config.phone
        case "email":
            return config.email
        case "logo":
            return config.logo.url
        case "keywords":
            return config.keywords
        case "author":
            return config.author
        case "description":
            return config.description
