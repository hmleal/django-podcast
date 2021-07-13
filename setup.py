from setuptools import setup
from pathlib import Path


CURRENT_DIR = Path(__file__).parent


def get_long_description():
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


setup(
    name="django-podcast",
    author="Henrique Leal",
    author_email="hm.leal@hotmail.com",
    version="0.0.1dev1",
    description="A small django app to easily publish podcasts",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/hmleal/django-podcast",
    install_requires=["Pillow"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 3.2",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
