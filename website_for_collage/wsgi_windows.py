import os
import sys
import site

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/Administrator/Documents/website_for_collage')
sys.path.append('C:/Users/Administrator/Documents/website_for_collage/website_for_collage')

os.environ['DJANGO_SETTINGS_MODULE'] = 'website_for_collage.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website_for_collage.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()