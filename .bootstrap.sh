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
which python2.7 || pyenv install 2.7.15
which python3.5 || LDFLAGS=-L/usr/lib/openssl-1.0 CFLAGS="-DOPENSSL_NO_SSL3 -I/usr/include/openssl-1.0" pyenv install 3.5.5
which python3.6 || pyenv install 3.6.5
which python3.7 || pyenv install 3.7.0
which pypy || pyenv install pypy2.7-6.0.0
which pypy3.5 || pyenv install pypy3.5-6.0.0

pyenv local 2.7.15 3.5.5 3.6.5 pypy2.7-6.0.0 pypy3.5-6.0.0

tmuxp load .tmuxp.yaml
