import io
import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def read(*names, **kwargs):
    """Read a file."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


setup(
    name="playlist",
    version=read("playlist", "VERSION"),
    url="https://github.com/hugoprudente/playlist-manager",
    license="APACHE",
    author="Hugo Prudente",
    author_email="hugo.kenshin@gmail.com",
    description="A playlist generator based on music databases",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "example",
            "example.*",
            "docs",
            "legacy_docs",
            "legacy_docs.*",
            "docs.*",
            "build",
            "build.*",
            "playlist.vendor_src",
            "playlist/vendor_src",
            "playlist.vendor_src.*",
            "playlist/vendor_src/*",
        ]
    ),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=["typing; python_version<'3.5'"],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-xdist",
        "flake8",
        "pep8-naming",
        "flake8-debugger",
        "flake8-print",
        "flake8-todo",
        "radon",
        "flask>=0.12",
        "python-dotenv",
        "toml",
        "codecov",
    ],
    # extras_require={
    # },
    entry_points={"console_scripts": ["playlist=playlist.cli:main"]},
    setup_requires=["setuptools>=38.6.0"]
    if sys.version_info >= (3, 6, 0)
    else [],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
