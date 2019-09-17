# Plex server with plex_autoscan
[![GitHub forks](https://img.shields.io/github/forks/horjulf/docker-plex_autoscan.svg?style=social&label=Fork&style=flat-square)](https://github.com/horjulf/docker-plex_autoscan)
[![Docker Pulls](https://img.shields.io/docker/pulls/horjulf/plex_autoscan.svg)](https://hub.docker.com/r/horjulf/plex_autoscan/)
[![](https://images.microbadger.com/badges/image/horjulf/plex_autoscan.svg)](https://microbadger.com/images/horjulf/plex_autoscan)

This image provides [plex_autoscan](https://github.com/l3uddz/plex_autoscan) on top of the plex server image from linuxserver.io([linuxserver/plex](https://hub.docker.com/r/linuxserver/plex/)).

## Usage

- Follow the instructions on [linuxserver/plex](https://hub.docker.com/r/linuxserver/plex/) for base image and plex server settings.

- plex_autoscan default config file will be created on first run, default locations are:
  - Folder will be created at: `/config/plex_autoscan`
  - Config file at: `/config/plex_autoscan/config.json`
  - Queue db file at: `/config/plex_autoscan/queue.db`
  - Log file at: `/config/plex_autoscan/plex_autoscan.log`

- plex_autoscan settings can be overwriten using ENV variables:
```
PLEX_AUTOSCAN_CONFIG
PLEX_AUTOSCAN_QUEUEFILE
PLEX_AUTOSCAN_LOGFILE
PLEX_AUTOSCAN_LOGLEVEL
```

- Check plex_autoscan [documentation](https://github.com/l3uddz/plex_autoscan/blob/master/README.md) for description of configuration settings.

### Examples

- Default config:
```shell
docker create \
--name=plex \
--net=host \
-e VERSION=latest \
-e PUID=<UID> -e PGID=<GID> \
-e TZ=<timezone> \
-v </path/to/library>:/config \
-v <path/to/tvseries>:/data/tvshows \
-v </path/to/movies>:/data/movies \
-v </path/for/transcoding>:/transcode \
horjulf/plex_autoscan
```

- Increase plex_autoscan logging and use different config file:
```shell
docker create \
--name=plex \
--net=host \
-e VERSION=latest \
-e PUID=<UID> -e PGID=<GID> \
-e TZ=<timezone> \
-e PLEX_AUTOSCAN_CONFIG=/config/plex_autoscan/custom_config.json \
-e PLEX_AUTOSCAN_LOGLEVEL=DEBUG \
-v </path/to/library>:/config \
-v <path/to/tvseries>:/data/tvshows \
-v </path/to/movies>:/data/movies \
-v </path/for/transcoding>:/transcode \
horjulf/plex_autoscan
```

- Plex_autoscan config paths:
```json
"PLEX_SCANNER": "/usr/lib/plexmediaserver/Plex\\ Media\\ Scanner",
"PLEX_SUPPORT_DIR": "/config/Library/Application\\ Support",
"PLEX_LD_LIBRARY_PATH": "/usr/lib/plexmediaserver/lib",
"PLEX_DATABASE_PATH": "/config/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db",
```
