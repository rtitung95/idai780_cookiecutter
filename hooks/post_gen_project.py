#!/usr/bin/env python
import os
import shutil
from pathlib import Path


def create_project_structure():
    """Create the project directory structure."""
    directories = [
        'scripts',
        'data',
        'models',
        'notebooks',
        'results',
        'figures',
    ]

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Create an empty __init__.py in each directory
        Path(os.path.join(directory, '__init__.py')).touch()


def main():
    create_project_structure()
    # Create LICENSE file if a license was selected
    if '{{ cookiecutter.open_source_license }}' != 'No license file':
        shutil.copy('hooks/license_template', 'LICENSE')

    shutil.move('hooks/test.png', 'figures/')


if __name__ == '__main__':
    main()
