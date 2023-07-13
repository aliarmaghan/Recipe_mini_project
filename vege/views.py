from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='/login/')
def recipes(request):
    
    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')


        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
       )

        return redirect('/recipes/')
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'page' : 'recipes', 'recipes': queryset}

    return render(request, "recipes.html",context)




@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')




@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')

    context = {'page' : 'Update_recipes', 'recipes': queryset}
    return render(request, "update_recipes.html",context)

def login_page(request):

    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid User name")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/recipes/")

    return render (request, 'login.html')


def logout_page(request):
   logout(request)
   return redirect('/login/')


def register(request):

    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username Already Exist")
            return redirect('/register/')

        user = User.objects.create(first_name = first_name,
                                   last_name = last_name,
                                   username = username,
                                   )
        
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")
        return redirect('/register/')
    
    return render (request, 'register.html')



from django.db.models import Q


def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) 
        )

    paginator = Paginator(queryset, 50)  # Show 50 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/student.html', {'queryset':page_obj})