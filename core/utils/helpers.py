import json
from django.http import JsonResponse
from django.core.files.base import ContentFile

def parse_json(request):
    """Parses JSON data from the request body."""
    try:
        return json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return {}

def handle_image_upload(image_data, filename="default_image.jpg"):
    """Handles image upload and creates a ContentFile."""
    if image_data:
        return ContentFile(image_data, name=filename)
    return None