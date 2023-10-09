---
title: "Private Apt Cache"
date: 2021-10-19T01:00:00
slug: 2021-10-19-private-apt-cache
type: post
draft: false
categories:
  - default
tags:
  - debian
  - docker
---

This how I've set up an apt package caching host. You may want this for:

1. Reducing the load you are putting on some upstream Debian package
   repository.
1. Kind of the same thing as the previous point, but framed differently:
   keeping as much traffic internal to your "stuff" as possible, perhaps
because it's cheaper.
1. Some amount of privacy regarding what packages you're downloading, when
   you're downloading them, and how many hosts you have that are using them.
1. It's kinda cool.

The gist is to create a webserver that pretends to be a Debian package
repository.  If it doesn't have something cached, it fetches it from upstream,
caches it, and forward it on to the requesting client host.

    $ cat Dockerfile
    FROM debian:bullseye
    RUN apt-get update -y && apt-get install -y \
    	nginx \
    	&& apt-get clean -y \
    	&& rm -r /var/lib/apt/lists/*
    COPY default /etc/nginx/sites-enabled/
    VOLUME /aptcache
    EXPOSE 80
    STOPSIGNAL SIGQUIT
    CMD ["nginx", "-g", "daemon off;"]

Next is the `default` file mentioned above which is an nginx config file.
Notice how I'm able to proxy requests to 3 different repositories.

    $ cat default
    proxy_cache_path /aptcache levels=1:2 keys_zone=aptcache:10m max_size=10g inactive=240h use_temp_path=off;
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        location /debian/ {
            proxy_cache aptcache;
            proxy_pass http://deb.debian.org/debian/;
        }
        location /debian-security/ {
            proxy_cache aptcache;
            proxy_pass http://security.debian.org/debian-security/;
        }
        location /torproject.org/ {
            proxy_cache aptcache;
            proxy_pass http://deb.torproject.org/torproject.org/;
        }
    }

.

From here we build and tag this image:

    $ docker build -t aptcache .

Then create a network to which we attach any containers that should have
access to this cache host, and create a volume for this host to store
cached data.

    $ docker network create aptcache
    $ docker volume create aptcache

Finally we run a container with this image.

    $ docker run \
        --detach \
        --restart always \
        --name aptcache \
        --network aptcache \
        --volume aptcache:/aptcache \
        aptcache

In the [next post]({{< ref using-private-apt-cache >}}) we'll use this apt
cache in a new base Debian image.
