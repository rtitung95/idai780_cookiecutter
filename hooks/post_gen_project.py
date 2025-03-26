#!/usr/bin/env python
import os
import shutil
from pathlib import Path

def create_project_structure():
    """Create the project directory structure."""
    directories = [
        'configs',
        'data',
        'models',
        'tools',
        'tests',
    ]
    
    # Add demo directory if specified
    if '{{ cookiecutter.include_demo }}' == 'y':
        directories.append('demo')
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Create an empty __init__.py in each directory
        Path(os.path.join(directory, '__init__.py')).touch()

def create_environment_file():
    """Create environment.yml with basic dependencies."""
    env_content = f'''name: {{{{ cookiecutter.project_slug }}}}
channels:
  - conda-forge
  - defaults
dependencies:
  - python={{{{ cookiecutter.python_version }}}}
  - pip
  - pytest
  - pip:
    - {{{{ cookiecutter.framework.lower() }}}'''
    
    with open('environment.yml', 'w') as f:
        f.write(env_content)

def create_setup_py():
    """Create setup.py for package installation."""
    setup_content = '''from setuptools import setup, find_packages

setup(
    name="{{{{ cookiecutter.project_slug }}}}",
    version="{{{{ cookiecutter.version }}}}",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="{{{{ cookiecutter.author_name }}}}",
    author_email="{{{{ cookiecutter.author_email }}}}",
    description="{{{{ cookiecutter.project_short_description }}}}",
    license="{{{{ cookiecutter.open_source_license }}}}",
    python_requires=">={{{{ cookiecutter.python_version }}}",
)'''
    
    with open('setup.py', 'w') as f:
        f.write(setup_content)

def init_git():
    """Initialize git repository."""
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Initial commit"')

def main():
    create_project_structure()
    create_environment_file()
    create_setup_py()
    
    # Create LICENSE file if a license was selected
    if '{{ cookiecutter.open_source_license }}' != 'No license file':
        # You would typically have a template for each license type
        pass
    
    # Initialize git repository
    init_git()

if __name__ == '__main__':
    main()
