---
layout: default
title: 🚀 Quick Start With Pulsarr
nav_order: 1
---

# 🚀 Quick Start With GitHub Pages

There are several ways to configure the Pulsarr bot to work with your discord server
I would recommend running this in docker

## Create discord application

First a discord application is required, this will be how the bot connects to discord

* Go to [Discord Developers](https://discordapp.com/developers/applications/me)
* Click `New Application`
* Enter a name `pulsarr`
* Click Create
* Click the `Bot` menu item
* Click `Add Bot`
* Click `Yes, do it!`
* Copy the `TOKEN`
* Open `config.yml`
* Paste the `TOKEN` next to `botToken:`
* Back on the Discord page go too `OAuth2`
* Tick `bot`
* Either select `Administrator`  or as a minimum:
  * `Read Messages`
  * `Send Messages`
  * `Manage Messages`
  * `Embed Links`
  * `Read Message History`
  * `Mention Everyone`
  * `Use External Emojis`
  * `Add Reactions`