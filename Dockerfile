FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1

# Install packages
RUN apt update \
    && apt install -y \
        wget \
        build-essential \
        zlib1g-dev \
        libssl-dev \
        libsqlite3-dev \
        locales \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Set locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install Python 3.9
RUN wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz \
    && tar zxf Python-3.9.6.tgz \
    && cd Python-3.9.6 \
    && ./configure --enable-optimizations \
    && make altinstall

# Set alias
RUN update-alternatives --install \
    /usr/local/bin/python3 python3 /usr/local/bin/python3.9 1

# Upgrade pip
RUN /usr/local/bin/python3.9 -m pip install -U pip

WORKDIR /shinya/mysite

CMD ["/bin/bash"]

