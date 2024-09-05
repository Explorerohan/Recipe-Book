from django.shortcuts import render,redirect
from .models import Recipe

# Create your views here.
def add_recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
        Recipe.objects.create(name=name, description=description,image=image)
    return render(request, 'add_recipes.html')

def view_recipes(request):
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        recipes =Recipe.objects.filter(name__icontains = request.GET.get('search'))    
    return render(request, 'view_recipes.html',{"recipes":recipes})

def delete_recipes(request,id):
    Recipes = Recipe.objects.get(id=id)
    Recipes.delete()
    return redirect('view-recipes')

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