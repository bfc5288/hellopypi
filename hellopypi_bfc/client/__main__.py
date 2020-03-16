#!/usr/bin/env python

__author__ = "bfc"

import argparse
import signal

from . import __version__

def set_up_cli():
    """Set up CLI commands for entry point.
    """
    parser = argparse.ArgumentParser(prog="hellopypi")
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s-client version {__version__}",
    )

    return parser

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = set_up_cli()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

