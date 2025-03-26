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
        'results'
    ]

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        Path(os.path.join(directory, '__init__.py')).touch()


def main():
    create_project_structure()


if __name__ == '__main__':
    main()
