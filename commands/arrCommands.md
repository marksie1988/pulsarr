---
layout: default
title: Arr Commands
nav_order: 1
---

# Arr Commands

Arr Commands are all of the commands that relate to Sonarr or Radarr functions

## search

The search allows you to find a TV Series or a Movie, this can be done via
a search term or TVDB ID

```shell
/pulsarr search show 'the walking dead'
```

![screenshot](../assets/images/screenshots/search-term.png)

```shell
/pulsarr search show 153021
```

![screenshot](../assets/images/screenshots/search-153021.png)

## status

This command will show you the status of the Sonarr & Radarr servers:

```shell
/pulsarr status
```

![screenshot](../assets/images/screenshots/status.png)

## diskSpace

Shows how much disk space is available on the Sonarr & Radarr volumes:

```shell
/pulsarr diskSpace
```

![screenshot](../assets/images/screenshots/diskSpace.png)