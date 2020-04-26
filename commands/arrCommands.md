---
layout: default
title: Arr Commands
parent: Commands
nav_order: 4
---

{:toc}

# Arr Commands

Arr Commands are all of the commands that relate to Sonarr or Radarr functions

## search

The search allows you to find a TV Series or a Movie, this can be done via
a search term or TVDB ID

```shell
/pulsarr search <series|movie> <term|tvdb>
```

### Examples

```shell
/pulsarr search series the walking dead
```

![screenshot](../assets/images/screenshots/search-term.png)

```shell
/pulsarr search series 153021
```

![screenshot](../assets/images/screenshots/search-153021.png)

## add

add will let you add a new series or movie to the library ready for download

```shell
/pulsarr add <series|movie> <tvdb|imdb> <quality-id>
```

Note: IMDB can only be used for movies at the moment due to limitations in the Sonarr API

### Example

```shell
/pulsarr add series 76316 1
```

![screenshot](../assets/images/screenshots/add-76316.png)

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

Gets the quality profiles from Sonarr & Radarr, assists with "Add" command:

```shell
/pulsarr quality <series|movie>
```

### Example

```shell
/pulsarr quality series
```

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
