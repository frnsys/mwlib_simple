#! /usr/bin/env python

# Copyright (c) 2007-2011 PediaPress GmbH
# See README.rst for additional licensing information.

import os, sys, glob
from setuptools import setup, Extension

def get_version():
    d = {}
    exec(compile(open("mwlib/_version.py").read(), "mwlib/_version.py", 'exec'), d, d)
    return str(d["version"])

def build_deps():
    err = os.system("make all")
    if err != 0:
        sys.exit("Error: make failed")


def main():
    if os.path.exists('Makefile'):
        build_deps()

    install_requires = ["lxml", "simplejson>=2.3"]

    ext_modules = []
    ext_modules.append(Extension("mwlib._uscan", ["mwlib/_uscan.cc"]))

    for x in glob.glob("mwlib/*/*.c"):
        modname = x[:-2].replace("/", ".")
        ext_modules.append(Extension(modname, [x]))

    setup(
        name="mwlib",
        version=get_version(),
        install_requires=install_requires,
        ext_modules=ext_modules,
        packages=["mwlib"],
        namespace_packages=['mwlib'],
        include_package_data=True,
        zip_safe=False,
        url="http://code.pediapress.com/",
        description="mediawiki parser and utility library",
        license="BSD License",
        maintainer="pediapress.com",
        maintainer_email="info@pediapress.com",
        long_description='')


if __name__ == '__main__':
    main()
