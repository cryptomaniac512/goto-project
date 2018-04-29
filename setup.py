from setuptools import setup

setup(
    author="Nikita Sivakov",
    author_email="sivakov.512@gmail.com",
    description="Easy and fast project switching in your shell!",
    install_requires=['PyYAML'],
    keywords="project shell management",
    license="MIT",
    long_description_markdown_filename='README.md',
    name="goto-project",
    packages=["goto_project"],
    python_requires='>=3.6',
    scripts=['goto_project/gt'],
    setup_requires=['setuptools-markdown'],
    url="https://github.com/sivakov512/goto-project",
    version="0.1.1",
)
