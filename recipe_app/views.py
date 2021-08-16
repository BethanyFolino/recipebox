from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

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

@login_required
def add_recipe(request):
    # if not request.user.is_staff:
    #     form = AddRecipeNonStaff(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         recipe = Recipe.objects.create(
    #             title=data['title'],
    #             author=data['author'],
    #             description=data['description'],
    #             time_required=data['time_required'],
    #             instructions=data['instructions']
    #         )
    #         return HttpResponseRedirect(reverse('home'))
    # form = AddRecipeNonStaff()
    # return render(request, 'generic_form.html', {'form': form})   
    
    if request.method == "POST":
        if request.user.is_staff:
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
        elif not request.user.is_staff:
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe = Recipe.objects.create(
                    title=data['title'],
                    author=data['author'],
                    description=['description'],
                    time_required=data['time_required'],
                    instructions=data['instructions']
                )
                return HttpResponseRedirect(reverse('home'))
            form = AddRecipeForm()

        return render(request, 'generic_form.html', {'form': form})

@login_required
def add_author(request):
    # if not request.user.is_staff:
    #     return HttpResponse('Non-staff users cannot add authors.')
    if not request.user.is_staff:
        messages.error(request, 'Non-staff users cannot add authors.', extra_tags='error')
        return HttpResponseRedirect(reverse('home'))
    if request.method == "POST" and request.user.is_staff:
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], password=data['password'])
            author = Author.objects.create(
                name = data['name'],
                bio = data['bio'],
                user= user
            )
            messages.success(request, 'Author successfully created!', extra_tags='success')
            return HttpResponseRedirect(reverse('home'))
    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                messages.success(request, 'Login successful!', extra_tags='success')
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))

    form = LoginForm()
    return render(request, 'generic_form.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!', extra_tags='success')
    return HttpResponseRedirect(request.GET.get('next', reverse('home')))