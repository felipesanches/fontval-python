from __future__ import absolute_import
import sys
import fval


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    return fval.run_checks(*args).returncode


if __name__ == "__main__":
    sys.exit(main())
