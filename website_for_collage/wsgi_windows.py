# Windows WSGI
import os
import sys
import site

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(os.path.join(BASE_DIR, 'env', 'Lib', 'site-packages'))


# Add the app's directory to the PYTHONPATH
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'website_for_collage.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website_for_collage.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()