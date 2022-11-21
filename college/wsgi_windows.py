# Windows WSGI
import os
import sys
import site
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(os.path.join(BASE_DIR, "env", "Lib", "site-packages"))

# Add the app's directory to the PYTHONPATH
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(__file__))

os.environ["DJANGO_SETTINGS_MODULE"] = "college.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
