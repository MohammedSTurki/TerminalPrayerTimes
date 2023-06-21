from setuptools import setup, find_packages

setup(
    name="Prayer Time Script",
    version="1.0",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    license='',
    author='Mohammed Salman Turki',
    author_email='mohammed.s.turki@gmail.com',
    description="A collection of scripts to view today's prayer times...",
    install_requires=['requests', 'pyfiglet', 'tabulate', 'pytest'],
    extras_require=dict(tests=['pytest'])
)