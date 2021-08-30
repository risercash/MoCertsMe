# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/c/cashriser/cashriser.beget.tech/HelloDjango')# /home/c/cashriser/mocerts.com/public_html/HelloDjango
sys.path.insert(1, '/home/c/cashriser/mocerts.com/public_html/venv/bin/python')
os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloDjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()