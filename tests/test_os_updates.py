#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyarchops_os_updates` package."""

from suitable import Api
from pyarchops_helpers.helpers import ephemeral_docker_container
from pyarchops_os_updates import os_updates


def test_os_updates_using_docker():
    """Test the OS updates."""

    with ephemeral_docker_container(
            image='registry.gitlab.com/pyarchops/pyarchops-base'
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
            result = os_updates.apply(api)['contacted'][connection_string]
        except Exception as error:
            raise error

        assert result['msg'] == 'System upgraded'
