"""
ASGI config for Festum project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# Festum/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Festum.settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import userApi.routing

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": AuthMiddlewareStack(
        URLRouter(  
            userApi.routing.websocket_urlpatterns
        )
    ),
})

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Festum.settings')

# application = get_asgi_application()



# import os
# from channels.routing import get_default_application
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
# django.setup()
# application = get_default_application()