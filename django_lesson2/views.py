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


def omlet(requests):
    servings = int(requests.GET.get("servings", 1))
    return HttpResponse(
        f"omlet\n яйца, шт: {2 * servings},\n молоко, л: {0.1 * servings},\n соль, ч.л.: {0.5 * servings}")


def pasta(request):
    servings = int(request.GET.get("servings", 1))
    return HttpResponse(f"pasta\n макароны, г: {0.3 * servings}, сыр, г: {0.05 * servings}")


def butter(request):
    servings = int(request.GET.get("servings", 1))
    return HttpResponse(f"butter\n хлеб, ломтик: {1 * servings},\n колбаса, ломтик: {1 * servings},\n сыр, ломтик: "
                        f"{1*servings},\n помидор, ломтик: {1*servings}")
