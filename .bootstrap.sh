#!/usr/bin/env bash
# .boostrap.sh
# install required python dependencies

bold=$(tput bold)
normal=$(tput sgr0)

echo "${bold}running bootstrap ....${normal}"


if [ ! -e .venv ]; then
    echo "${bold}initializing virtualenv...${normal}"
    virtualenv --python=`which python` .venv
    source .venv/bin/activate
    echo "${bold}installing python requirements...${normal}"
    pip install -r requirements.txt
    echo "${bold}installing development python requirements...${normal}"
    pip install -r requirements_dev.txt
    echo "${bold}installing local source...${normal}"
    pip install -e .
  fi


if ! `which pyenv >/dev/null 2>&1`; then
    if ! `test -e .pyenv`; then
        echo "${bold}installing pyenv locally....${normal}"
        git clone https://github.com/pyenv/pyenv.git .pyenv
    fi
fi

if `test -e .pyenv`; then
    echo "${bold}.pyenv found, using local pyenv${normal}"
    export PYENV_ROOT="$PWD/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
fi


which pyenv

echo "${bold}activating  pyenv....${normal}"
eval "$(pyenv init -)"

echo "${bold}activating  venv....${normal}"
source .venv/bin/activate

local_python_version=`cat .python-version`

if ! `pyenv versions | grep ${local_python_version} >/dev/null 2>&1`; then
    echo "${bold}installing python version ${local_python_version} using pyenv${normal}"
    pyenv install ${local_python_version}
fi

echo "${bold}running test for the first time....${normal}"
test -e .tox || tox

echo "${bold}finished bootstrapping...${normal}"
