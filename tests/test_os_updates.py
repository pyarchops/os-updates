#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `archops_os_updates` package."""

import os
import re
from contextlib import contextmanager
from archops_os_updates import os_updates
from fabric.context_managers import settings, hide, quiet
from fabric.api import local
from suitable import Api
import netifaces
import time


# TODO: all this functions should be oved to a
# archops.helpers package on pypi



@contextmanager
def ephemeral_docker_container(**kwargs):
    """
        prepares a docker container, yelding a dict
        with its configuration before deleting the container

    """
    try:
        container_id = docker_up(image=kwargs['image'])

        yield dict({
            'user': 'root',
            'ip': dockerd_ip(),
            'port': docker_container_port(container_id),
            'pkey': 'tests/fixtures/id_rsa'
        })
        #docker_down(container_id)
        #docker_rm(container_id)
    except Exception as error:
        print('jhsajdfhdsf')
        #docker_down(container_id)
        #docker_rm(container_id)


def docker_up(image, privileged=False):
    """
        runs a docker container

        params:
            string image: name of the docker image
            bool privileged: use docker --privileged flag
        returns:
            string: stdout of the docker run
    """

    flags = ''
    if privileged:
        flags = '--privileged'

    container_id = local(
        "docker run --privileged -ti "
        " -v /sys/fs/cgroup:/sys/fs/cgroup:ro "
        " -d -P {} {}".format(flags, image),
        capture=True
    )
    return container_id


def docker_down(container_id):
    """
        kills the docker container

        params:
            string container: docker id of the container to stop
    """
    with settings(quiet()):
        local('docker kill %s' % container_id)


def docker_rm(container_id):
    """
        removes a docker container

        params:
            string container: docker id of the container to remove
    """
    with settings(quiet()):
        local('docker rm --force %s' % container_id)


def docker_container_port(container_id):
    """
        returns the ssh port number for a docker instance

        params:
            string container: docker container id

        returns:
            string: port number
    """
    with settings(quiet()):
        output = local(
            'docker port %s 22' % container_id,
            capture=True
        )

        return output.split(':')[1]


def dockerd_ip():
    """
        returns the ip address of the docker daemon

        params:
            string docker_host_string: URL of the docker daemon
        returns:
            string: ip address of the docker host
    """
    if 'DOCKER_HOST' in os.environ:
        docker_host_env = os.environ.get('DOCKER_HOST')
        ipaddr = re.search(
            r'[tcp|http]:\/\/(.*):\d.*', docker_host_env).group(1)  # noqa
    else:
        ipaddr = netifaces.ifaddresses(
            'docker0')[netifaces.AF_INET][0]['addr']
    return ipaddr



def test_os_updates_using_docker():
    """Test the OS updates."""

    with ephemeral_docker_container(image='azulinho/archops-base') as container:
        connection_string = "{}:{}".format(
            container['ip'], container['port']
        )
        time.sleep(1)
        print('connection strings is ' + connection_string)
        api = Api(connection_string,
                  connection='smart',
                  remote_user=container['user'],
                  private_key_file=container['pkey'],
                  become=True,
                  become_user='root',
                  sudo=True)

        try:
            result = os_updates.apply(api)
            print(dir(result))
            # TODO: this never gets executed on error
            print(dir(result))
        except Exception as error:
            print(error)
            raise error
        # I need an assert here
