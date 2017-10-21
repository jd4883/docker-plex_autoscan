FROM linuxserver/plex

RUN \
  # Install dependencies
  apt-get update && \
  apt-get full-upgrade -y && \
  apt-get install --no-install-recommends -y \
    git \
    python \
    python-pip \
    python-dev \
    g++ && \
  # Get plex_autoscan
  git clone --depth 1 --single-branch https://github.com/l3uddz/plex_autoscan.git /plex_autoscan && \
  # Install/update pip and requirements
  pip install --no-cache-dir --upgrade pip setuptools && \
  pip install --no-cache-dir --upgrade -r /plex_autoscan/requirements.txt && \
  # Remove dependencies
  apt-get purge -y --auto-remove \
    python-dev \
    g++ && \
  # Clean apt cache
  apt-get clean all && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

COPY root/ /

# Plex_autoscan config file
ENV PLEX_AUTOSCAN_CONFIG=/config/plex_autoscan/config.json
# Plex_autoscan queue db file
ENV PLEX_AUTOSCAN_QUEUEFILE=/config/plex_autoscan/queue.db
# Plex_autoscan log file
ENV PLEX_AUTOSCAN_LOGFILE=/config/plex_autoscan/plex_autoscan.log
# Plex_autoscan disable docker and sudo
ENV USE_DOCKER=false
ENV USE_SUDO=false
