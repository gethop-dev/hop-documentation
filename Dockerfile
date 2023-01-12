FROM ubuntu:22.04

WORKDIR /hop-docs

RUN apt-get update && \
    apt-get install -y runit python3 python3-virtualenv && \
    apt-get clean && \
    mkdir -p /venv && python3.10 -mvirtualenv /venv && \
    /venv/bin/python -m pip install --upgrade --no-cache-dir 'pip' 'setuptools<58.3.0' && \
    /venv/bin/python -m pip install --upgrade --no-cache-dir 'pillow' 'mock==1.0.1' 'alabaster>=0.7,<0.8,!=0.7.5' 'commonmark==0.9.1' 'recommonmark==0.5.0' 'sphinx' 'sphinx-rtd-theme' 'readthedocs-sphinx-ext<2.3' 'sphinx-autobuild'

COPY run-as-user.sh /usr/local/bin

EXPOSE 8080

ENTRYPOINT ["run-as-user.sh"]

CMD /venv/bin/sphinx-autobuild \
    --port 8080 \
    --host 0.0.0.0 \
    -j auto \
    -T \
    -E \
    -b html \
    -D language=en \
    -d docs/_build/doctrees \
    docs/source \
    docs/_build/html
