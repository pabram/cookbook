from django.shortcuts import render
from recipes.models import Category, Recipe
from recipes.forms import CategoryForm, RecipeForm, UserForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime


def index(request):
    category_list = Category.objects.order_by('-views')[:5]
    most_viewed = Recipe.objects.order_by('-views')[:3]
    second_most = Recipe.objects.order_by('-views')[3:6]
    context_dict = {'categories': category_list, 'most_viewed': most_viewed, 'second_most': second_most}
    return render(request, 'recipes/index.html', context_dict)


def about(request):
    return render(request, 'recipes/about.html')


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None

    return render(request, 'recipes/category.html', context_dict)


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'recipes/add_category.html', {'form': form})


@login_required
def add_recipe(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            if category:
                recipe = form.save(commit=False)
                recipe.category = category
                recipe.views = 0
                recipe.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'recipes/add_recipe.html', context_dict)


def show_recipe(request, category_name_slug, recipe_name_slug):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        context_dict['recipe'] = recipe
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'recipes/recipe.html', context_dict)

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')
