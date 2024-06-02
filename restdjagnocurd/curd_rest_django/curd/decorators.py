# myapp/decorators.py
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def csrf_exempt_method_decorator(view):
    return method_decorator(csrf_exempt, name=view)
