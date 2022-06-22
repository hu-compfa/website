import os
import sys
import site


# Add the app's directory to the PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'website_for_collage.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website_for_collage.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()