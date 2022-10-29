"""
WSGI config for ts13 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# When running on Azure App Service you should use the production settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ts13.production' if 'WEBSITE_HOSTNAME' in os.environ else 'ts13.development')

application = get_wsgi_application()