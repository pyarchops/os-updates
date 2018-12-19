#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `archops_os_updates` package."""

from suitable import Api
from archops_os_updates import os_updates
from tests.test_helpers import ephemeral_docker_container


def test_os_updates_using_docker():
    """Test the OS updates."""

    with ephemeral_docker_container(
            image='azulinho/archops-base'
    ) as container:
        connection_string = "{}:{}".format(
            container['ip'], container['port']
        )
        print('connection strings is ' + connection_string)
        api = Api(connection_string,
                  connection='smart',
                  remote_user=container['user'],
                  private_key_file=container['pkey'],
                  become=True,
                  become_user='root',
                  sudo=True,
                  ssh_extra_args='-o StrictHostKeyChecking=no')

        try:
            result = os_updates.apply(api)
            print(dir(result))
            # TODO: this never gets executed on error
            print(dir(result))
        except Exception as error:
            print(error)
            raise error
        # I need an assert here
