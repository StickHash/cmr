from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='addid')
def addid(value, arg):
    return value.as_widget(attrs={'id': arg})


@register.filter(name='addclass_and_id')
def addclassandid(value, args):
    arg_list = args.split(',')
    return value.as_widget(attrs={'class': arg_list[0], 'id': arg_list[1]})
