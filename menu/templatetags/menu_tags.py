from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    """
    Render the menu with the given `menu_name` in the template `menu/menu.html`.
    
    Args:
        context (dict): The context containing the request object.
        menu_name (str): The name of the menu to render.
    
    Returns:
        dict: A dictionary containing the menu items and the active item.
            - menu_items (QuerySet): The menu items filtered by the given menu name.
            - active_item (MenuItem): The active menu item, or None if there is no active item.
    """
    request = context["request"]
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related("parent")
    active_item = None
    for item in menu_items:
        if item.get_absolute_url() == request.path:
            active_item = item
            break
    return {
        "menu_items": menu_items,
        "active_item": active_item,
    }
