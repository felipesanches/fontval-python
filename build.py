#!/usr/bin/env python3
"""Run meson and ninja to build the ots-sanitize executable from source.

NOTE: This script requires Python 3.6 or above. However the generated binary
is independent from the python version used to run it.
"""
import sys
from pathlib import Path
import os
import subprocess
import shutil
import errno
import argparse

version = "2.1.2" #FIXME! Auto-detect this.
ROOT = Path(__file__).parent.resolve()
SRC_DIR = ROOT.joinpath("src", "cs", "fval")

TOOLS = {
    "make": os.environ.get("MAKE_EXE", "make"),
}

MAKE_CMD = [
  TOOLS["make"]
]

class ExecutableNotFound(FileNotFoundError):
    def __init__(self, name, path):
        msg = f"{name} executable not found: '{path}'"
        super().__init__(errno.ENOENT, msg)


def check_tools():
    for name, path in TOOLS.items():
        if shutil.which(path) is None:
            raise ExecutableNotFound(name, path)


def configure(reconfigure=False):
    pass


def make(*targets, clean=False):
    targets = list(targets)
    print (f"Targets are: {targets}")
    _env = '\n'.join([f"{k}:\t\t{v}" for k,v in os.environ.items()])
    print ("os.getcwd(): {}".format(os.getcwd()))
    os.chdir(SRC_DIR)
    print ("os.getcwd(): {}".format(os.getcwd()))
    #subprocess.run(MAKE_CMD + targets, check=True, env=os.environ)
    subprocess.run(MAKE_CMD, check=True, env=os.environ)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true")
    parser.add_argument("targets", nargs="*")
    options = parser.parse_args(args)

    check_tools()

    try:
        configure(reconfigure=options.force)

        make(*options.targets, clean=options.force)
    except subprocess.CalledProcessError as e:
        return e.returncode


if __name__ == "__main__":
    sys.exit(main())
