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
/pulsarr search <series|movie> <term|tvdb>
```


```shell
/pulsarr search series the walking dead
```

![screenshot](../assets/images/screenshots/search-term.png)

```shell
/pulsarr search series 153021
```

![screenshot](../assets/images/screenshots/search-153021.png)

## getfolder

getFolder will display the root folder for either Radarr or Sonarr

```shell
/pulsarr getfolder <series|movie>
```

### Example

```shell
/pulsarr getfolder series
```

## quality

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
