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
which python3.7 || pyenv install 3.7.0
which pypy3.5 || pyenv install pypy3.5-6.0.0

pyenv local 3.7.0 pypy3.5-6.0.0

test -e .tox || tox
tmuxp load .tmuxp.yaml
