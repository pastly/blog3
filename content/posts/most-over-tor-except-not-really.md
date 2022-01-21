---
title: "Mosh over Tor (Except Not Really)"
date: 2017-06-18
slug: 2017-06-18-mosh-over-tor-except-not-really
type: posts
draft: false
categories:
  - default
tags:
  - mosh
  - onion-service
---

*This post first appeared on my old blog in June 2017. It is preserved, but
maybe not updated, here.*

---

I'm in the process of setting up a new server and I'm trying to be super ultra
mega secure about it. It's running FreeBSD with some fancy security options
enabled, blah blah blah, oh and I made SSH over Tor the only way to remotely
access it for administration. It's a
[[private onion service|creating-private-onion-GmiiUPQL]],
which is super cool in itself, but since I don't mind leaking the location of
this server, it is also a single-onion service. This does seem to have a
positive impact on the speed and latency to the machine, but after a few weeks
of managing the machine completely over Tor, I determined I wanted more
usability.

My main complaint is the lack of immediate local echoing of what I type. Mosh
does that, but mosh uses UDP, which doesn't work over Tor. There's two ways I
could approach this. The first would actually be called "Mosh over Tor," but I
ultimately went for the second as it would actually allow me to roam (another
great feature of mosh).

1. I could use socat to tunnel UDP over Tor. Create the tunnel and then mosh to
`localhost:some-port`.

2. Or I could authenticate over SSH over Tor and then create the actual UDP
connection over the regular Internet. 

So I now present to you the script I use to (not really) use mosh over Tor. It's
a healthy mixture of things specific to me and hardcoded values that need
changing for every use case. But it is a starting point if you would like to
try your hand at (2) above too.

    #!/usr/bin/env bash
    MOSH_IP="ip.of.remotehost.foo"
    SSH_HOSTNAME="hostname.foo.from.ssh.config"
    SUCCESS_LINE=$(ssh $SSH_HOSTNAME "mosh-server new -i $MOSH_IP" | grep 'MOSH CONNECT')
    [[ "$SUCCESS_LINE" == "" ]] && echo "failed to connect :(" && exit 1
    MOSH_PORT=$(echo $SUCCESS_LINE | cut -d ' ' -f 3)
    
    export MOSH_KEY="$(echo $SUCCESS_LINE | cut -d ' ' -f 4)"
    mosh-client $MOSH_IP $MOSH_PORT

At its core, mosh first authenticates you over SSH. It then runs `mosh-server`
on the server and passes some information back to your local computer. It then
uses that information to tell `mosh-client` how to connect to the server. All
I've done here is do all that manually (in what is probably a bad,
easily-broken, and I-am-lucky-it-works way).

So if you save the above script as `moshfoo`, make it executable, put it
in your PATH, and fix the `MOSH_IP` variable to be the public IP of the server
foo, then you can run

    moshfoo

and assuming ssh can figure out how to connect and authenticate you, everything
will work out wonderfully.

Do you have a better way to accomplish local echo when SSHing into an onion
service? Do you want to call me stupid? Or perhaps inform me that I'm blind for
missing an obvious solution or glaring problem? Please let me know!
