from django.shortcuts import render

def home(request):
    return render(request, '../templates/home.html')

def about(request):
    return render(request, '../templates/about.html')

from core.models import Project
def projects(request):
    projects = Project.objects.all()
    return render(request, '../templates/projects.html', {'projects': projects})

from core.models import Contact
from django.shortcuts import redirect

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')  # Redirect after submission
    return render(request, '../templates/contact.html')

from core.models import BlogPost

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, '../templates/blog.html', {'posts': posts})