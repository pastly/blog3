---
title: "Minimal Debian Base Image for Docker"
date: 2021-10-18
slug: 2021-10-18-minimal-debian-base-image-for-docker
type: post
draft: false
categories:
  - default
tags:
  - debian
  - docker
---

1. Be on a Debian host.
1. Install debootstrap.
1. Have docker.
1. Do this, but replace all instances of bullseye with whatever version of
   Debian you want.

.

    $ debootstrap --variant=minbase bullseye bullseye-minbase
    $ ls
    bullseye-minbase
    $ tar -C bullseye-minbase -c . | docker import - bullseye-minbase

Done.

https://wiki.debian.org/Debootstrap  
https://docs.docker.com/develop/develop-images/baseimages/
