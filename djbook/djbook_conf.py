# to apply these settings add to conf.py
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "djbook")))
# from djbook_conf import *
import sys
import os

html_theme_path = ["_theme", "djbook/_theme"]
html_theme = "djbook"

language = 'ru'
locale_dirs = ['./locale/']
exclude_patterns = ['_build', 'djbook', 'env']
gettext_compact = False
