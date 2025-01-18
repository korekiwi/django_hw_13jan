def menu_items(request):
    menu = [
    {"title": "Главная", "url_name": "main"},
    {"title": "О проекте", "url_name": "about"},
    {"title": "Все посты", "url_name": "blog:posts"},
    {"title": "Категории", "url_name": "blog:categories"},
    {"title": "Теги", "url_name": "blog:tags"},
]
    
    current_url_name = request.resolver_match.view_name
    
    for item in menu:
        item['is_active'] = current_url_name == item['url_name']
    
    return {'menu_items': menu}