from argparse import ArgumentParser
from typing import Callable
from taxonid._version import __version__
from brs_utils import add_logger_args


def build_args_parser(
    prog: str,
    description: str = '',
    epilog: str = '',
    m_add_args: Callable = None,
) -> ArgumentParser:

    parser = ArgumentParser(
        prog=prog,
        description=description,
        epilog=epilog
    )

    # Build Parser with rptools common arguments
    parser = _add_arguments(parser)

    # Add module specific arguments
    if m_add_args is None:
        parser = add_arguments(parser)
    else:
        parser = m_add_args(parser)

    return parser


def _add_arguments(parser: ArgumentParser) -> ArgumentParser:
    # Add arguments related to the logger
    parser = add_logger_args(parser)

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(__version__),
        help='show the version number and exit'
    )

    return parser


def add_arguments(parser: ArgumentParser) -> ArgumentParser:

    parser.add_argument(
        'org_name',
        type=str,
        help='Name of the organism to get taxon ID'
    )
    parser.add_argument(
        '--output-file',
        '-o',
        type=str,
        default=None,
        help='Filename to save the taxon ID'
    )

    return parser
