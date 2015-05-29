from setuptools import setup, find_packages

"""
    for the long description, convert:
        https://coderwall.com/p/qawuyq
    or manually here:
        http://johnmacfarlane.net/pandoc/try/
"""

def check_java_version():
    import re
    from subprocess import STDOUT, check_output
    out = check_output(["java".encode("utf-8"), "-version".encode("utf-8")], stderr=STDOUT).split("\n".encode("utf-8"))
    if len(out) < 1:
        print("failed checking Java version. Make sure Java version 7 or greater is installed.")
        return False
    m = re.match('java version "\d+.(\d+)..*'.encode("utf-8"), out[0])
    if m is None or len(m.groups()) < 1:
        print("failed checking Java version. Make sure Java version 7 or greater is installed.")
        return False
    java_version = int(m.group(1))
    if java_version < 7:
        error_msg = "Found Java version %d, but Java version 7 or greater is required." % java_version

        raise RuntimeError(error_msg)

def check_java_exists():
    from subprocess import call
    import os
    try:
        devnull = open(os.devnull, 'w')
        call("java", stdout=devnull, stderr=devnull)
    except:
        error_msg = """
        Java not found!

        pysmac needs java in order to work. You can download java from:
        http://java.com/getjava
        """
        raise RuntimeError(error_msg)

check_java_exists()
check_java_version()

setup(
    name = "pysmac",
    version = "0.9",
    packages = find_packages(),
    install_requires = ['docutils>=0.3', 'setuptools', 'numpy', 'matplotlib', 'pynisher'],
    dependency_links=['https://github.com/sfalkner/pynisher/archive/master.zip#egg=pynisher'],
    #dependency_links=['https://github.com/sfalkner/pynisher/master'],
    author = "Stefan Falkner and Tobias Domhan (python wrapper). Frank Hutter, Holger Hoos, Kevin Leyton-Brown, Kevin Murphy and Steve Ramage (SMAC)",
    author_email = "sfalkner@informatik.uni-freiburg.de",
    description = "python interface to the hyperparameter optimization tool SMAC.",
    include_package_data = True,
    keywords = "hyperparameter parameter optimization hyperopt bayesian smac global",
    license = "SMAC is free for academic & non-commercial usage. Please contact Frank Hutter(fh@informatik.uni-freiburg.de) to discuss obtaining a license for commercial purposes.",
    url = "http://www.cs.ubc.ca/labs/beta/Projects/SMAC/"
)
