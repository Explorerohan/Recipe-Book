from django.shortcuts import render
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
    return render(request, 'view_recipes.html',{"recipes":recipes})