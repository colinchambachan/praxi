"""
WSGI config for praxi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from react_templates.wsgi import get_web_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'praxi.settings')

application = get_wsgi_application()
web_application = get_web_application()