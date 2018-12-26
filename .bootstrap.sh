#!/usr/bin/env bash
# .boostrap.sh
# install required python dependencies

bold=$(tput bold)
normal=$(tput sgr0)

echo "${bold}running bootstrap ....${normal}"


if ! `which pyenv >/dev/null 2>&1`; then
    echo "${bold}installing pyenv....${normal}"
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.profile
    echo 'eval "$(pyenv init -)"' >> ~/.profile
fi

echo "${bold}activating  pyenv....${normal}"
. ~/.profile

echo "${bold}looking for a new pyenv version....${normal}"
pyenv update

local_python_version=`cat .python-version`

if ! `pyenv versions | grep ${local_python_version} >/dev/null 2>&1`; then
    echo "${bold}installing python version ${local_python_version} using pyenv${normal}"
    pyenv install ${local_python_version}
fi

if [ ! -e .venv ]; then
    echo "${bold}initializing virtualenv...${normal}"
    virtualenv --python=`which python` .venv
    echo "${bold}activating  venv....${normal}"
    . .venv/bin/activate
    echo "${bold}installing python requirements...${normal}"
    pip install -r requirements.txt
    echo "${bold}installing development python requirements...${normal}"
    pip install -r requirements_dev.txt
    echo "${bold}installing local source...${normal}"
    pip install -e .
fi

echo "${bold}finished bootstrapping...${normal}"
