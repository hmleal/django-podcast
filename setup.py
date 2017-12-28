from setuptools import setup

try:
    from pypandoc import convert_file

    def read_md(filename):
        return convert_file(filename, 'rst')
except ImportError:
    print('warning: pypandoc module not found, could not convert Markdown to RST')


setup(
    name='django-podcast',
    author='Henrique Leal',
    author_email='hm.leal@hotmail.com',
    version='0.0.1dev0',
    description='A small django app to easily publish podcasts',
    long_description=read_md('README.md'),
    url='https://github.com/hmleal/django-podcast',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
