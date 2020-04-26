---
layout: default
title: Config File
nav_order: 2
---

# Config File

The configuration file stores all of the required congif to get the bot started,
at a later date I plan on moving over to a database to support multiple discord servers

You can start by copying the file from `.stubs/config.yml` to the root directory

## Options

Then you can customise the file as needed with the possible options:

| Name | Type | Requirement | Since | Description |
|------|:----:|:-------:|:-----:|-------------|
| botName | string | **required** | v0.1.0 | What you would like your bot to be called
| botToken | string | **required** | v0.1.0 | Your discord bot token
| botPrefix | string | **required** | v0.1.0 | `/pulsarr ` Preferred prefix to call the bot commands
| sonarr.host | string | **required** | v0.1.0 | `https:\\sonarr.yourserver.com` Address to your Sonarr server, must include http
| sonarr.token | string | **required** | v0.1.0 | Token from Sonarr
| radarr.host | string | **required** | v0.1.0 | `https:\\radarr.yourserver.com` Address to your Radarr server, must include http
| radarr.token | string | **required** | v0.1.0 | Token from Radarr

## Example Configuration

```yaml
botName: pulsarr
botToken: Njasodh12h3QWEDWETH41on23.GPa1234.tS8ASDSDWWWASDDFFFASD
botPrefix: "/pulsarr "
sonarr:
    host: https://sonarr.yourserver.com
    token: asdkmoihjs123932157usajijdn
radarr:
    host:
    token:

```
