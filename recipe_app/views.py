from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'homepage.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'recipes': recipes})

def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe.objects.create(
                title=data['title'], 
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddRecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = Author.objects.create(
                name = data['name'],
                bio = data['bio']
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddAuthorForm()
    return render(request, 'add_author.html', {'form': form})