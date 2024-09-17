from django.shortcuts import render,redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Creating my views here.
@login_required(login_url='/')
def add_recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
        Recipe.objects.create(name=name, description=description,image=image)
    return render(request, 'add_recipes.html')

@login_required(login_url="/")
def view_recipes(request):
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        recipes =Recipe.objects.filter(name__icontains = request.GET.get('search'))    
    return render(request, 'view_recipes.html',{"recipes":recipes})

@login_required(login_url="/")
def delete_recipes(request,id):
    Recipes = Recipe.objects.get(id=id)
    Recipes.delete()
    return redirect('view-recipes')


@login_required(login_url="/")
def update_recipes(request,id):
    recipes = Recipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        recipes.name = data.get('name')
        recipes.description = data.get('description')
        image = request.FILES.get('image')
        if image:
            recipes.image = image
        recipes.save()
        return redirect('view-recipes')
    return render(request, 'update_recipes.html', {'recipes': recipes})

def signup_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,"Username already exist.")
            return redirect('signup-page')
        user = User.objects.filter(email=email)
        if user.exists():
            messages.error(request,"Email address already used.")
            return redirect('signup-page')
        user = User.objects.create(username = username, email = email)
        user.set_password(password)
        user.save()
        messages.success(request,"Successfully Created Account. Remember to login.")
    return render(request, 'signup_page.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('login-page')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('view-recipes')
        else:
            messages.error(request,'Invalid Password')
            return redirect('login-page')
    return render(request, 'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('login-page')
