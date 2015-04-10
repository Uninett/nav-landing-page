import sys
import os

if not os.path.exists(os.path.join(os.path.dirname(globals()['__file__']), 'base.py')):
    sys.stderr.write("Failed to locate the base settings file. Quitting.\n")
    sys.exit(1)
try:
    from nav_landing_page.settings.base import *
except ImportError:
    sys.stderr.write("Failed to import from the base settings file. Quitting.\n")
    sys.exit(1)
