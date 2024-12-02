from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from core.models import Project
from core.utils.helpers import parse_json, handle_image_upload

@csrf_exempt
def project_list(request):
    """Handles GET and POST requests for projects."""
    if request.method == 'GET':
        projects = Project.objects.all()
        data = [
            {
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'technologies': project.technologies,
                'live_link': project.live_link,
                'repo_link': project.repo_link,
                'image_url': project.image.url if project.image else None,
            }
            for project in projects
        ]
        return JsonResponse({'projects': data})
    elif request.method == 'POST':
        data = parse_json(request)
        image_data = data.get('image')
        image_file = handle_image_upload(image_data, "project_image.jpg")
        project = Project.objects.create(
            title=data.get('title', 'Untitled Project'),
            description=data.get('description', ''),
            technologies=data.get('technologies', ''),
            live_link=data.get('live_link', ''),
            repo_link=data.get('repo_link', ''),
            image=image_file
        )
        return JsonResponse({'message': 'Project created successfully', 'id': project.id})

@csrf_exempt
def project_detail(request, project_id):
    """Handles GET, PUT, and DELETE requests for a specific project."""
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'GET':
        data = {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'technologies': project.technologies,
            'live_link': project.live_link,
            'repo_link': project.repo_link,
            'image_url': project.image.url if project.image else None,
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = parse_json(request)
        project.title = data.get('title', project.title)
        project.description = data.get('description', project.description)
        project.technologies = data.get('technologies', project.technologies)
        project.live_link = data.get('live_link', project.live_link)
        project.repo_link = data.get('repo_link', project.repo_link)
        project.save()
        return JsonResponse({'message': 'Project updated successfully'})
    elif request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'Project deleted successfully'})
