import os
import sys

# assuming your django settings file is at '/home/TedRose/mysite/mysite/settings.py'
# and your manage.py is is at '/home/TedRose/mysite/manage.py'
path = '/home/TedRose/Django_course/personal_portfolio-project/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'personal_portfolio.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
