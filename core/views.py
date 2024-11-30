from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from .models import Project
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

from .models import Contact
from django.shortcuts import redirect

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')  # Redirect after submission
    return render(request, 'contact.html')

from .models import BlogPost

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})
