def paginate(iterable, per_page, page_num):
    """
        recipes = Recipe.objects.all()
        paginator, recipes = paginate(recipes, 12, 
            request.GET.get('page', '1'))
    """
    from django.core.paginator import Paginator, InvalidPage, EmptyPage

    paginator = Paginator(iterable, per_page)

    try:
        page = int(page_num)
    except ValueError:
        page = 1

    try:
        iterable = paginator.page(page)
    except (EmptyPage, InvalidPage):
        iterable = paginator.page(paginator.num_pages)

    return paginator, iterable