# FROM gitpod/workspace-python

USER gitpod

RUN pyenv install 3.9 \
    && pyenv global 3.9
