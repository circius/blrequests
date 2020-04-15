import setuptools
from glob import glob
from os.path import basename
from os.path import splitext

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blrequests",
    version="0.0.1",
    author="circius",
    author_email="circius@posteo.de",
    description="CLI British Library catalogue",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/circius/bl-requests",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console :: Curses",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    keywords=["british-library", "cli"],
    python_requires=">=3.6",
    setup_requires=["pytest-runner",],
    install_requires=["Click", "beautifulsoup4", "tabulate",],
    entry_points="""
    [console_scripts]
    blrequests=blrequests.cli:cli
""",
)
