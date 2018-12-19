#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Helpers for `archops tests` packages."""

# TODO: all this functions should be oved to a
# archops.helpers package on pypi

import os
import re
import time
import socket
from contextlib import contextmanager
from fabric.api import local
from fabric.context_managers import settings, quiet
import paramiko
from paramiko.ssh_exception import (
    AuthenticationException,
    BadHostKeyException,
    SSHException
)
import netifaces


def wait_for_ssh(host, initial_wait=0, interval=0, retries=1):
    """ waits for ssh to become available """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    time.sleep(initial_wait)

    for _ in range(retries):
        try:
            ssh.connect(host['ip'], username=host['user'], port=host['port'])
            return True
        except (AuthenticationException, BadHostKeyException):
            return True
        except (SSHException, socket.error) as error:
            print(error)
            time.sleep(interval)
    return False


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
        docker_down(container_id)
        docker_rm(container_id)
    except Exception as error:
        docker_down(container_id)
        docker_rm(container_id)
        raise error


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
        " --cpu-period=100000 --cpu-quota=10000 "
        " -v /sys/fs/cgroup:/sys/fs/cgroup:ro "
        " -d -P {} {}".format(flags, image),
        capture=True
    )
    host = {
        'ip': dockerd_ip(),
        'user': 'root',
        'port': docker_container_port(container_id)
    }
    wait_for_ssh(
        host=host,
        initial_wait=1,
        retries=10,
        interval=1
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
