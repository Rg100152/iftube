#!/usr/bin/env python3
"""
IFTUBE - YouTube Metadata & OSINT Scanner
Setup script for packaging and distribution
Owner: Raj Gautam
GitHub: https://github.com/Rg100152/iftube
"""

import os
import re
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.test import test as TestCommand

# ============================================================
# VERSION EXTRACTION
# ============================================================

def get_version():
    """Extract version from the main module"""
    with open('iftube.py', 'r', encoding='utf-8') as f:
        content = f.read()
        version_match = re.search(r"VERSION\s*=\s*['\"]([^'\"]+)['\"]", content)
        if version_match:
            return version_match.group(1)
    return '1.0.0'

def get_author():
    """Extract author from the main module"""
    with open('iftube.py', 'r', encoding='utf-8') as f:
        content = f.read()
        author_match = re.search(r"OWNER\s*=\s*['\"]([^'\"]+)['\"]", content)
        if author_match:
            return author_match.group(1)
    return 'Raj Gautam'

def get_description():
    """Extract description from the main module"""
    with open('iftube.py', 'r', encoding='utf-8') as f:
        content = f.read()
        desc_match = re.search(r'"""([^"]+)"""', content)
        if desc_match:
            return desc_match.group(1).strip()
    return 'YouTube Metadata & OSINT Scanner'

# ============================================================
# README EXTRACTION
# ============================================================

def read_readme():
    """Read README.md content"""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return get_description()

def read_requirements():
    """Read requirements from requirements.txt"""
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            requirements = []
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('='):
                    # Remove version specifiers for core dependencies
                    if not any(skip in line for skip in ['pytest', 'flake8', 'pylint', 'black', 'sphinx']):
                        requirements.append(line.split('#')[0].strip())
            return requirements
    return [
        'requests>=2.28.0',
        'beautifulsoup4>=4.11.0',
        'yt-dlp>=2023.12.30',
        'tabulate>=0.9.0',
        'lxml>=4.9.0'
    ]

# ============================================================
# CUSTOM INSTALL COMMANDS
# ============================================================

class CustomInstall(install):
    """Custom install command with post-install hooks"""
    
    def run(self):
        """Run install with post-install message"""
        install.run(self)
        self.show_post_install_message()
    
    def show_post_install_message(self):
        """Display post-installation instructions"""
        print("\n" + "="*60)
        print("🎉 IFTUBE installed successfully!")
        print("="*60)
        print("\n📌 Quick Start:")
        print("   $ iftube")
        print("   or")
        print("   $ python -m iftube")
        print("\n📚 Documentation:")
        print("   https://github.com/Rg100152/iftube")
        print("\n💡 Need help?")
        print("   $ iftube --help")
        print("="*60 + "\n")

class CustomDevelop(develop):
    """Custom develop command"""
    
    def run(self):
        """Run develop with post-install message"""
        develop.run(self)
        print("\n✅ IFTUBE installed in development mode")
        print("📝 Changes to the code will be reflected immediately")

class PyTest(TestCommand):
    """Custom test command for pytest"""
    
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]
    
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []
    
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    
    def run_tests(self):
        """Run pytest with arguments"""
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# ============================================================
# SETUP CONFIGURATION
# ============================================================

setup(
    # Basic Information
    name='iftube',
    version=get_version(),
    author=get_author(),
    author_email='rg100152@example.com',
    description=get_description(),
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rg100152/iftube',
    
    # Package Information
    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'docs']),
    include_package_data=True,
    package_data={
        'iftube': ['data/*.json', 'data/*.yaml', 'config/*.conf'],
    },
    zip_safe=False,
    
    # Dependencies
    python_requires='>=3.6',
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'pytest-xdist>=3.0.0',
            'flake8>=6.0.0',
            'pylint>=2.15.0',
            'black>=23.0.0',
            'isort>=5.12.0',
            'mypy>=1.0.0',
            'types-requests>=2.28.0',
            'types-beautifulsoup4>=4.11.0',
        ],
        'gui': [
            'PyQt5>=5.15.0',
            'PyQtWebEngine>=5.15.0',
        ],
        'web': [
            'flask>=2.2.0',
            'flask-cors>=3.0.0',
            'flask-restx>=1.0.0',
        ],
        'analytics': [
            'pandas>=1.5.0',
            'numpy>=1.23.0',
            'nltk>=3.8.0',
            'textblob>=0.17.0',
            'scikit-learn>=1.2.0',
        ],
        'cloud': [
            'google-api-python-client>=2.0.0',
            'boto3>=1.26.0',
            'azure-storage-blob>=12.0.0',
        ],
        'docs': [
            'sphinx>=6.0.0',
            'sphinx-rtd-theme>=1.2.0',
            'myst-parser>=1.0.0',
        ],
        'full': [
            'PyQt5>=5.15.0',
            'flask>=2.2.0',
            'pandas>=1.5.0',
            'numpy>=1.23.0',
            'nltk>=3.8.0',
            'google-api-python-client>=2.0.0',
            'boto3>=1.26.0',
            'sphinx>=6.0.0',
        ]
    },
    
    # Entry Points
    entry_points={
        'console_scripts': [
            'iftube=iftube:main',
            'iftube-scan=iftube:main',
        ],
        'gui_scripts': [
            'iftube-gui=iftube.gui:main',
        ],
    },
    
    # Classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Education',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Environment :: X11 Applications :: Qt',
        'Natural Language :: English',
    ],
    
    # Keywords
    keywords=[
        'youtube', 'metadata', 'scanner', 'osint', 'analysis',
        'video', 'info', 'extractor', 'analytics', 'youtube-api',
        'youtube-scraper', 'video-metadata', 'yt-dlp', 'information-gathering',
        'osint-tool', 'youtube-analytics', 'metadata-extractor',
        'video-analyzer', 'youtube-info', 'youtube-stats'
    ],
    
    # Project URLs
    project_urls={
        'Bug Reports': 'https://github.com/Rg100152/iftube/issues',
        'Source': 'https://github.com/Rg100152/iftube',
        'Documentation': 'https://github.com/Rg100152/iftube/wiki',
        'Changelog': 'https://github.com/Rg100152/iftube/releases',
        'Author': 'https://github.com/Rg100152',
    },
    
    # Command Classes
    cmdclass={
        'install': CustomInstall,
        'develop': CustomDevelop,
        'test': PyTest,
    },
    
    # Additional Options
    test_suite='tests',
    tests_require=['pytest>=7.0.0'],
    
    # Setup Requirements
    setup_requires=[
        'setuptools>=65.0.0',
        'wheel>=0.40.0',
    ],
    
    # Build Options
    options={
        'build': {
            'build_base': 'build',
        },
        'bdist_wheel': {
            'universal': True,
            'python_tag': 'py3',
        },
    },
)

# ============================================================
# POST-SETUP VALIDATION
# ============================================================

def validate_setup():
    """Validate setup configuration"""
    import sys
    print("="*60)
    print("🔍 Validating IFTUBE setup...")
    print("="*60)
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6+ is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check required files
    required_files = ['iftube.py', 'README.md', 'requirements.txt']
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"⚠️  {file} missing")
    
    # Check package structure
    packages = find_packages()
    if packages:
        print(f"✅ Found packages: {', '.join(packages)}")
    else:
        print("⚠️  No packages found")
    
    print("="*60 + "\n")

if __name__ == '__main__':
    validate_setup()
    setup()
