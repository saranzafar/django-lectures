from django import template

register = template.Library()

# 1. 
# def myreplace(value, arg):
#     return value.replace(arg, 'we are')

# register.filter('iamToweare', myreplace)

# 2. 
@register.filter(name='iamToweare')
def myreplace(value, arg):
    return value.replace(arg, 'we are')