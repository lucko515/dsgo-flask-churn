#!/usr/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ChurnApp/")

from ChurnApp import app as application
application.secret_key = '3sda2G!~S@3Gsa#DSA'