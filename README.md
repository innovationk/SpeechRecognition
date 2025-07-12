# SpeechRecognition

## Prerequisites

### pyenv

Build Dependencies

Ubuntu/Debian:
    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

macOS: 
    brew install openssl readline sqlite3 xz zlib


Using the pyenv-installer

    curl https://pyenv.run | bash


Enable Pyenv.

macOS:
    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    source ~/.zprofile # Or just restart your terminal

Test
    pyenv --version
    pyenv install --list
    pyenv install --list | grep "3.12"

This will install pyenv along with a few plugins that are useful:

    pyenv: The actual pyenv application
    pyenv-virtualenv: Plugin for pyenv and virtual environments
    pyenv-update: Plugin for updating pyenv
    pyenv-doctor: Plugin to verify that pyenv and build dependencies are installed
    pyenv-which-ext: Plugin to automatically lookup system commands


### Python

    pyenv install -v 3.12.11
    pyenv local 3.12.11
    python -V

## Launch

    pip install vosk
    python vosk/main.py

    python _mozillaDeepSpeech/main.py