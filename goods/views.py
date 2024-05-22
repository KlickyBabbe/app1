from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Футболка белая",
                "description": "Крутая белая футболка из хлопка",
                "price": 800.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Футболка черная",
                "description": "Крутая черная футболка из хлопка",
                "price": 800.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Штаны белые",
                "description": "Белые штаны из футера чтобы попа не замерзла",
                "price": 1100.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Штаны черные",
                "description": "Черные штаны из футера чтобы попа не замерзла",
                "price": 1100.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Штаны серые",
                "description": "Серые штаны, но только для дома",
                "price": 1100.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Худи белое",
                "description": "Белое худи ваще суперское",
                "price": 1300.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Худи черное",
                "description": "Черное худи ваще суперское",
                "price": 1300.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Лонгслив белый",
                "description": "Крутой белый лонгслив, если вы знаете что это",
                "price": 900.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Лонгслив черный",
                "description": "Крутой черный лонгслив, если вы знаете что это",
                "price": 900.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Майка белая",
                "description": "Майка-алкоголичка для реальных пацанов",
                "price": 550.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Кайф",
                "description": "натуральный",
                "price": 10000000.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Нарды",
                "description": "Для кайфа",
                "price": "бесценно",
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
