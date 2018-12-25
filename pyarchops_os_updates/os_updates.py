# -*- coding: utf-8 -*-

"""Main module."""

import suitable


def apply(api: suitable.api.Api, quiet: bool = False) -> dict:
    """ installs os_updates """
    result = api.pacman(update_cache=True)
    result = api.pacman(upgrade=True)
    if not quiet:
        print(result['contacted'])
    return dict(result)
