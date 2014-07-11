#!/usr/bin/python
import os, sys

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi',
    'm10'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'm10.settings'

virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
