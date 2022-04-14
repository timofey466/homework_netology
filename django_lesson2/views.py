from django.http import HttpResponse
from django.shortcuts import render

data = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }}


def dish(request, recipe):
    serving = int(request.GET.get('serving', 1))
    recipe = data.get(recipe).copy()
    for key, value in data.items():
        recipe[key] = int(value) * serving
    context = {"recipe": recipe}
    return render(request, 'calculator/food.html', context)


