from setuptools import setup, find_packages
import re

with open("version.py", "r") as f:
    version = re.search(r"__version__ = '(.+)'", f.read()).group(1)

setup(
    name='hikkatl',
    version=version,
    description="Full-featured Telegram client library for Python 3",
    long_description="Hikka Telegram Library - MTProto client library for Python 3",
    
    url='https://github.com/hikariatama/Hikka',
    
    author='Lonami Exo & Dan Gazizullin',
    author_email='me@hikariatama.ru',
    
    license='AGPL-3.0',
    
    python_requires='>=3.8',
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    keywords='telegram api chat client library messaging mtproto',
    
    packages=find_packages(exclude=['tests*']),
    
    install_requires=[
        'pyaes',
        'rsa',
        'cryptg;platform_system!="Windows"'
    ],
    
    extras_require={
        'cryptg': ['cryptg']
    }
) 