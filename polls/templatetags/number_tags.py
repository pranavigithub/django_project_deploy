from django import template
register = template.Library()


@register.filter
def to_amount(value):  # only one argument.
    """change the number to amount format"""
    return f"{value:,}"

@register.filter
def full_name(fname, lname):
    return f"{fname.capitalize()} {lname.capitalize()}"


