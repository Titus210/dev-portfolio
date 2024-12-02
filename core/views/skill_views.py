from django.http import JsonResponse
from core.models import Skill

def skill_list(request):
    """Handles GET requests for skills."""
    if request.method == 'GET':
        skills = Skill.objects.all()
        data = [
            {
                'id': skill.id,
                'name': skill.name,
                'proficiency': skill.proficiency
            }
            for skill in skills
        ]
        return JsonResponse({'skills': data})
