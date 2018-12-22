#!/usr/bin/env bash
# .boostrap.sh
# install required python dependencies


echo "running bootstrap ...."

if [ ! -e .venv ]; then
    echo "initializing virtualenv..."
    virtualenv --python=`which python` .venv
    source .venv/bin/activate
    echo "installing python requirements..."
    pip install -r requirements.txt
    echo "installing development python requirements..."
    pip install -r requirements_dev.txt
    echo "installing local source..."
    pip install -e .
  fi


if ! `which pyenv >/dev/null 2>&1`; then
    if ! `test -e .pyenv`; then
        echo "installing pyenv locally...."
        git clone https://github.com/pyenv/pyenv.git .pyenv
    fi
fi

if `test -e .pyenv`; then
    echo ".pyenv found, using local pyenv"
    export PYENV_ROOT="$PWD/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
fi


which pyenv

echo "activating  pyenv...."
eval "$(pyenv init -)"

echo "activating  venv...."
source .venv/bin/activate

local_python_version=`cat .python-version`

if ! `pyenv versions | grep ${local_python_version} >/dev/null 2>&1`; then
    echo "installing python version ${local_python_version} using pyenv"
    pyenv install ${local_python_version}
fi

echo "running test for the first time...."
test -e .tox || tox

echo "finished bootstrapping..."
