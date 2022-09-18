"""
WSGI config for ts13 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from sol.ext_data import b200

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ts13.settings')

application = get_wsgi_application()

b200()