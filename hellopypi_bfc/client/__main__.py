#!/usr/bin/env python

__author__ = "bfc"

import argparse
import signal

from . import __version__
from . import testfunc

def append_subparser(subparser, cmd, func):
    assert func.__doc__, "empty docstring: {}".format(func)
    help_ = func.__doc__.split("\n")[0].lower().strip(".")
    desc = func.__doc__.strip()

    parser = subparser.add_parser(
        cmd,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        help=help_,
        description=desc,
    )

    parser.set_defaults(func=func)
    return parser
    
def set_up_cli():
    """Set up CLI commands for entry point.

    """
    parser = argparse.ArgumentParser(prog="hellopypi")
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s-client version {__version__}",
    )

    # set up subparser
    
    subparser = parser.add_subparsers(title='Commands', metavar='<command>', dest='cmd')
    subparser.required = True

    # register commands
    p = append_subparser(subparser, 'testfunc', testfunc._main)
    testfunc._add_parser_args(p)

    return parser


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    parser = set_up_cli()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
