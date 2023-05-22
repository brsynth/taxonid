from argparse import (
    ArgumentParser,
    Namespace
)
from logging import Logger
from colored import fg, attr

from .Args import (
    build_args_parser,
)
from .taxonid import get_taxon_id


def init(
    parser: ArgumentParser,
    args: Namespace
) -> Logger:

    from brs_utils import create_logger
    from taxonid._version import __version__

    if args.log.lower() in ['silent', 'quiet'] or args.silent:
        args.log = 'CRITICAL'

    # Create logger
    logger = create_logger(parser.prog, args.log)

    logger.info(
        '{color}{typo}{prog} {version}{rst}{color}{rst}\n'.format(
            prog=logger.name,
            version=__version__,
            color=fg('white'),
            typo=attr('bold'),
            rst=attr('reset')
        )
    )
    logger.debug(args)

    return logger


def entry_point():
    parser = build_args_parser(
        prog='taxonid',
        description='Get taxon ID from NCBI taxonomy database',
    )
    args = parser.parse_args()

    logger = init(parser, args)

    taxon_id = get_taxon_id(org_name=args.org_name, logger=logger)
    print(taxon_id)


if __name__ == '__main__':
    entry_point()
