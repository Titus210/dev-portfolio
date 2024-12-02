from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from core.models import Contact
from core.utils.helpers import parse_json
from core.utils.validators import validate_contact_details

@csrf_exempt
def submit_contact_message(request):
    """Handles POST requests for submitting contact messages."""
    if request.method == 'POST':
        data = parse_json(request)
        
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        try:
            # Validate the submitted data
            validate_contact_details(name, email, message)

            # Create a new Contact instance
            contact = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            return JsonResponse({'message': 'Contact message submitted successfully'}, status=201)

        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)

        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=500)

@csrf_exempt
def get_all_contacts(request):
    """Handles GET requests for fetching all contact messages."""
    if request.method == 'GET':
        try:
            contacts = Contact.objects.all().values('id', 'name', 'email', 'message', 'submitted_at')
            return JsonResponse({'contacts': list(contacts)}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=500)
