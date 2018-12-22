#!/usr/bin/env bash

if [ ! -e .venv ]; then
    virtualenv --python=`which python` .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements_dev.txt
    pip install -e .
  fi

which pyenv || (test -e .pyenv || git clone https://github.com/pyenv/pyenv.git .pyenv )
test -e .pyenv && export PYENV_ROOT="$PWD/.pyenv"
test -e .pyenv && export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init -)"

source .venv/bin/activate

# install required python versions
(pyenv versions | grep 3.7.1) || pyenv install 3.7.1

pyenv local 3.7.1

test -e .tox || tox
