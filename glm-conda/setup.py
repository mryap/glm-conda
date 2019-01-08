from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='glm-conda',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Testing",
    author="YAPSS",
    author_email='mryap@live.ie',
    url='https://github.com/mryap/glm-conda',
    packages=['glm-conda'],
    entry_points={
        'console_scripts': [
            'glm-conda=glm-conda.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='glm-conda',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
