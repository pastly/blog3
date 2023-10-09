---
title: "Using Private Apt Cache"
date: 2021-10-19T02:00:00
slug: 2021-10-19-using-private-apt-cache
type: post
draft: false
categories:
  - default
tags:
  - debian
  - docker
---

In the [previous post]({{< ref private-apt-cache >}}) we built a docker image
for an apt package cache. Here we will use it as part of a new base Debian
image, from which future feature-filled images can be based on.

This will appear a little extra difficult only because I want to include
torproject.org's Debian package repository. I'll call out below what you can
ingore if you only want Debian's repos.

First the Dockerfile.

    $ cat Dockerfile
    FROM debian:bullseye
    COPY sources.list /etc/apt/sources.list
    # Don't include any of the following if you don't want to add additional
    # sources.
    RUN apt-get update -y && apt-get install -y gnupg && rm -r /var/lib/apt/lists/*
    COPY *.asc .
    RUN cat *.asc | apt-key add -
    RUN rm *.asc
    COPY torproject.list /etc/apt/sources.list.d/
    RUN apt-get autoremove gnupg -y && rm -r /var/lib/apt/lists/*

Now the sources files. Notice the hostname is 'aptcache'.

    $ cat sources.list
    deb     http://aptcache/debian/         bullseye          main
    deb-src http://aptcache/debian/         bullseye          main
    deb     http://aptcache/debian/         bullseye-updates  main contrib non-free
    deb-src http://aptcache/debian/         bullseye-updates  main contrib non-free
    deb     http://aptcache/debian-security bullseye-security main contrib non-free
    deb-src http://aptcache/debian-security bullseye-security main contrib non-free
    # Don't include torproject.list if you don't want to use their repo.
    $ cat torproject.list 
    deb     http://aptcache/torproject.org/ bullseye main
    deb-src http://aptcache/torproject.org/ bullseye main

Finally the `.asc` file(s) for any custom repos. I have one (Tor's), and I
used [these instructions](https://support.torproject.org/apt/tor-deb-repo/) to help
me find the key with which they sign their packages.

    # It's a big ASCII-armored blob, and you don't need it if you don't want
    # Tor's repos.
    $ cat A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | wc -l
    771

Now we can build the image. Note we use the `aptcache` network during building
in order to use our caching webserver. **This is the key**.

    $ docker build --network aptcache -t debianbase:bullseye .

The first time we use the cache, we see things go relatively slowly. See the
last line of this snippit.

    [...]
    Get:18 http://aptcache/debian bullseye/main amd64 gpg-wks-client amd64 2.2.27-2 [523 kB]
    Get:19 http://aptcache/debian bullseye/main amd64 gpg-wks-server amd64 2.2.27-2 [516 kB]
    Get:20 http://aptcache/debian bullseye/main amd64 gpgsm amd64 2.2.27-2 [645 kB]
    Get:21 http://aptcache/debian bullseye/main amd64 gnupg all 2.2.27-2 [825 kB]
    Get:22 http://aptcache/debian bullseye/main amd64 libgpm2 amd64 1.20.7-8 [35.6 kB]
    Get:23 http://aptcache/debian bullseye/main amd64 libldap-common all 2.4.57+dfsg-3 [95.9 kB]
    Get:24 http://aptcache/debian bullseye/main amd64 libsasl2-modules amd64 2.1.27+dfsg-2.1 [104 kB]
    debconf: delaying package configuration, since apt-utils is not installed
    Fetched 9475 kB in 4s (2545 kB/s)
    [...]

But if we build the the image again (and this time use `--no-cache` so that
docker doesn't use existing intermediate images), we see the package fetching
goes much faster.

    $ docker build --no-cache --network aptcache -t debianbase:bullseye .
    [...]
    Get:18 http://aptcache/debian bullseye/main amd64 gpg-wks-client amd64 2.2.27-2 [523 kB]
    Get:19 http://aptcache/debian bullseye/main amd64 gpg-wks-server amd64 2.2.27-2 [516 kB]
    Get:20 http://aptcache/debian bullseye/main amd64 gpgsm amd64 2.2.27-2 [645 kB]
    Get:21 http://aptcache/debian bullseye/main amd64 gnupg all 2.2.27-2 [825 kB]
    Get:22 http://aptcache/debian bullseye/main amd64 libgpm2 amd64 1.20.7-8 [35.6 kB]
    Get:23 http://aptcache/debian bullseye/main amd64 libldap-common all 2.4.57+dfsg-3 [95.9 kB]
    Get:24 http://aptcache/debian bullseye/main amd64 libsasl2-modules amd64 2.1.27+dfsg-2.1 [104 kB]
    debconf: delaying package configuration, since apt-utils is not installed
    Fetched 9475 kB in 0s (159 MB/s)
    [...]

<small>Note: the `--no-cache` option has nothing to do with our package cache.
The flag is a docker thing to speed up builds when lines near the end of a
Dockerfile change; we're creating a proxy to Debian repositories that
intercepts HTTP requests and stores the responses for future use.</small>

Now going forward, whenever you build a new image based on `debianbase`, as
long as you include `--network aptcache` when you call `docker build`, you will
use the package cache. You can't forget it, otherwise you'll get error messages
such as this:

    $ docker build .
    Sending build context to Docker daemon  2.048kB
    Step 1/2 : FROM debianbase:bullseye
     ---> 578298174bde
    Step 2/2 : RUN apt-get update -y && apt-get install -y htop && rm -r /var/lib/apt/lists/*
     ---> Running in 43c2e275628c
    Err:1 http://aptcache/debian bullseye InRelease
      Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    Err:2 http://aptcache/debian bullseye-updates InRelease
      Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    Err:3 http://aptcache/debian-security bullseye-security InRelease
      Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    Err:4 http://aptcache/torproject.org bullseye InRelease
      Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    Reading package lists...
    W: Failed to fetch http://aptcache/debian/dists/bullseye/InRelease  Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    W: Failed to fetch http://aptcache/debian/dists/bullseye-updates/InRelease  Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    W: Failed to fetch http://aptcache/debian-security/dists/bullseye-security/InRelease  Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    W: Failed to fetch http://aptcache/torproject.org/dists/bullseye/InRelease  Something wicked happened resolving 'aptcache:80' (-5 - No address associated with hostname)
    W: Some index files failed to download. They have been ignored, or old ones used instead.
    Reading package lists...
    Building dependency tree...
    Reading state information...
    E: Unable to locate package htop
    The command '/bin/sh -c apt-get update -y && apt-get install -y htop && rm -r /var/lib/apt/lists/*' returned a non-zero code: 100
