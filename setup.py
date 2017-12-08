from distutils.core import setup
setup(
    name = 'instaget',
    packages = ['instaget'],
    version = '0.2.1',
    install_requires = [
            "requests",
            "bs4",
    ],

    entry_points = {
        'console_scripts': [
            'instaget = instaget.__main__:main'
        ]
    },

    description = 'CLI tool for downloading Instagram pictures',
    author = 'Juanjo Salvador',
    author_email = 'juanjosalvador@netc.eu',
    url = 'https://github.com/juanjosalvador/instaget', # use the URL to the github repo
    download_url = 'https://github.com/juanjosalvador/instaget/archive/0.1.tar.gz', # I'll explain this in a second
    keywords = ['instagram', 'downloader'], # arbitrary keywords
    classifiers = [],
)