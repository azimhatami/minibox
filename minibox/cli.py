import os
from os import path

import easycli


def issystemfile(filename):
    abspath_ = path.abspath(filename)
    base = path.basename(abspath_)
    return base.startswith('.')


class Show(easycli.SubCommand):
    __command__ = 'show'

    def __call__(self, args):
        for root, dirs, files in os.walk('.'):
            if issystemfile(root):
                continue
            items = ' '.join([i for i in dirs + files if not issystemfile(i)])
            print(f'{root}:\n{items}\n')


class Minibox(easycli.Root):
    __completion__ = True
    __arguments__ = [
        easycli.Argument(
            '-v', '--version',
            action='store_true',
            help='Show version'
        ),
        Show,
    ]

    def __call__(self, args):
        if args.version:
            from minibox import __version__
            print(__version__)
            return

        return super().__call__(args)
