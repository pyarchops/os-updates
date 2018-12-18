# -*- coding: utf-8 -*-

"""Main module."""


def apply(api, quiet=False):
    """ installs os_updates """
    result = api.pacman(update_cache=True)
    result = api.pacman(upgrade=True)
    if not quiet:
        print(result['contacted'])
    return result
