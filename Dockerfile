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
  pip3 install --no-cache-dir --upgrade -r requirements.txt && \
  # Remove dependencies
  apt-get purge -y --auto-remove \
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

COPY root/ scripts /

ENV \
  CRYPT_MAPPINGS="" \
  # Plex_autoscan disable docker and sudo
  DOCKER_NAME="plex" \
  GOOGLE_DRIVE_CLIENT_ID="" \
  GOOGLE_DRIVE_CLIENT_SECRET="" \
  GOOGLE_DRIVE_ENABLED=false \
  GOOGLE_DRIVE_FILE_EXTENSIONS=true \
  GOOGLE_DRIVE_FILE_EXTENSIONS_LIST= \
  GOOGLE_DRIVE_FILE_PATHS="" \
  GOOGLE_DRIVE_MIME_TYPES= \
  GOOGLE_DRIVE_MIME_TYPES_LIST= \
  GOOGLE_DRIVE_POLL_INTERVAL= \
  GOOGLE_DRIVE_SHOW_CACHE_LOGS= \
  GOOGLE_DRIVE_TEAMDRIVE= \
  GOOGLE_DRIVE_TEAMDRIVES= \
  PLEX_ANALYZE_DIRECTORY= \
  PLEX_ANALYZE_TYPE= \
  PLEX_AUTOSCAN_CACHEFILE=/config/plex_autoscan/cache.db \
  # Plex_autoscan cache db
  PLEX_AUTOSCAN_CONFIG=/config/plex_autoscan/config.json \
  # Plex_autoscan config file
  PLEX_AUTOSCAN_LOGFILE=/config/plex_autoscan/plex_autoscan.log \
  # Plex_autoscan log file
  PLEX_AUTOSCAN_QUEUEFILE=/config/plex_autoscan/queue.db \
  # Plex_autoscan queue db
  PLEX_CHECK_BEFORE_SCAN=false \
  PLEX_DATABASE_PATH="/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db" \
  PLEX_EMPTY_TRASH=false \
  PLEX_EMPTY_TRASH_CONTROL_FILES="" \
  PLEX_EMPTY_TRASH_MAX_FILES=100 \
  PLEX_EMPTY_TRASH_ZERO_DELETED=false \
  PLEX_FIX_MISMATCHED=false \
  PLEX_FIX_MISMATCHED_LANG="en" \
  PLEX_LD_LIBRARY_PATH="/usr/lib/plexmediaserver/lib" \
  PLEX_LOCAL_URL="http://localhost:32400" \
  PLEX_SCANNER="/usr/lib/plexmediaserver/Plex Media Scanner" \
  PLEX_SUPPORT_DIR="/var/lib/plexmediaserver/Library/Application Support" \
  PLEX_TOKEN="ChangeMe" \
  PLEX_USER="plex" \
  PLEX_WAIT_FOR_EXTERNAL_SCANNERS=true \
  RCLONE_BINARY="" \
  RCLONE_CACHE_REFRESH_ENABLED=false \
  RCLONE_CACHE_REFRESH_FILE_EXISTS_TO_REMOTE_MAPPINGS="" \
  RCLONE_CONFIG="" \
  RCLONE_URL="http://localhost:5572" \
  RUN_COMMAND_AFTER_SCAN="" \
  RUN_COMMAND_BEFORE_SCAN="" \
  SERVER_FILE_CHECK_DELAY=60 \
  SERVER_FILE_EXIST_PATH_MAPPINGS="" \
  SERVER_IGNORE_LIST="" \
  SERVER_IP="0.0.0.0" \
  SERVER_MAX_FILE_CHECKS=10 \
  SERVER_PASS="ChangeMe" \
  SERVER_PATH_MAPPINGS="" \
  SERVER_PORT=3468 \
  SERVER_SCAN_DELAY=180 \
  SERVER_SCAN_FOLDER_ON_FILE_EXISTS_EXHAUSTION=false \
  SERVER_SCAN_PRIORITIES="" \
  SERVER_USE_SQLITE=true \
  USE_DOCKER=false \
  USE_SUDO=false

RUN python3 scripts/config_builder.py
