"""
ASGI config for ts13 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

# When running on Azure App Service you should use the production settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ts13.production' if 'WEBSITE_HOSTNAME' in os.environ else 'ts13.development')

application = get_asgi_application()
