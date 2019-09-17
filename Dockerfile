FROM linuxserver/plex:latest

ARG PLEX_AUTOSCAN_BRANCH="master"

RUN \
  # Install dependencies
  apt-get update && \
  apt-get full-upgrade -y && \
  apt-get install --no-install-recommends -y \
    git \
    python3 \
    python3-pip \
    python3-dev \
    g++ && \
  # Get plex_autoscan
  git clone --depth 1 --single-branch --branch ${PLEX_AUTOSCAN_BRANCH} https://github.com/l3uddz/plex_autoscan.git /plex_autoscan && \
  # Install/update pip and requirements
  pip3 install --no-cache-dir --upgrade pip setuptools wheel && \
  # PIP upgrade bug https://github.com/pypa/pip/issues/5221
  hash -r pip3 && \
  pip3 install --no-cache-dir --upgrade -r /plex_autoscan/requirements.txt && \
  # Remove dependencies
  apt-get purge -y --auto-remove \
    git \
    python3-dev \
    g++ && \
  # Link python to python3
  ln -s /usr/bin/python3 /usr/bin/python && \
  # Clean apt cache
  apt-get clean all && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

COPY root/ /

ENV \
  # Plex_autoscan config file
  PLEX_AUTOSCAN_CONFIG=/config/plex_autoscan/config.json \
  # Plex_autoscan queue db
  PLEX_AUTOSCAN_QUEUEFILE=/config/plex_autoscan/queue.db \
  # Plex_autoscan log file
  PLEX_AUTOSCAN_LOGFILE=/config/plex_autoscan/plex_autoscan.log \
  # Plex_autoscan cache db
  PLEX_AUTOSCAN_CACHEFILE=/config/plex_autoscan/cache.db \
  # Plex_autoscan disable docker and sudo
  USE_DOCKER=false \
  USE_SUDO=false
