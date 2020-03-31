#!/usr/bin/env python

__author__ = 'bfc'

import argparse

def say_hello(message):
    '''Say hello and print a message.
    '''

    print('Hello there! I am here to tell you ' +str(message))


# main

def _add_parser_args(parser):
    parser.add_argument(
        "-m",
        "--message",
        required=True,
        help="A message to print for the user.",
        dest="message",
    )
    
def _main(args=None):
    '''Read and print messages.
    '''

    if not args:
        parser = argparse.ArgumentParser()
        _add_parser_args(parser)
        args = parser.parse_args()

    # load options
    msg = 'the default message'

    if args.message:
        msg = args.message

    # print the message

    say_hello(msg)
