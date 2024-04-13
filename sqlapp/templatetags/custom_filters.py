from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    try:
        fields = list(form)
        current_index = fields.index(form[current_field])
        return fields[current_index + 1].name if current_index + 1 < len(fields) else None
    except (ValueError, IndexError):
        return None

@register.filter
def to(value, arg):
    """ 指定された範囲の数値のリストを生成 """
    return range(value, arg + 1)


@register.filter
def get_attribute(obj, attr_name):
    """ オブジェクトから指定された属性を取得 """
    return getattr(obj, attr_name, None)

@register.filter
def concatenate(value, arg):
    return f"{value}{arg}"