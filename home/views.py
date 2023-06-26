from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(requset):

    people = [
        {'name' : 'Md Ali', 'age' : 24},
        {'name' : 'Md Danish', 'age' : 25},
        {'name' : 'Md Saifi', 'age' : 24},
        {'name' : 'Rupa', 'age' : 12},
        {'name' : 'Md Talha', 'age' : 23},
        {'name' : 'Radha', 'age' : 2},
        {'name' : 'Md Azam', 'age' : 26},
    ]

    text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    vegetables = ['Pumpkin','Tomato','Potato']

    return render(requset,"index.html", context={'page' : 'This is Django page','peoples' : people, 'text' : text, 'vegetables': vegetables} )


def success_page(requset):
    return HttpResponse("<h1>Hyy this is django Success Page</h1>")


def about(request):
    context = {'page' : 'About'}
    return render(request, "about.html",context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html",context)