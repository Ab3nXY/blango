#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

if __name__ == "__main__":
    # Set DJANGO_CONFIGURATION environment variable
    os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

    # Set default Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blango.settings")

    try:
        from configurations.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )

    execute_from_command_line(sys.argv)
