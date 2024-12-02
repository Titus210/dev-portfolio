import re
from django.core.exceptions import ValidationError

def validate_contact_details(name, email, message):
    """Validates contact details submitted by the user."""
    if not name or len(name.strip()) == 0:
        raise ValidationError("Name is required and cannot be empty.")
    
    if not re.match(r'^[a-zA-Z\s]+$', name):
        raise ValidationError("Name must only contain letters and spaces.")
    
    if not email or len(email.strip()) == 0:
        raise ValidationError("Email is required.")
    
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise ValidationError("Invalid email format.")
    
    if not message or len(message.strip()) == 0:
        raise ValidationError("Message cannot be empty.")
