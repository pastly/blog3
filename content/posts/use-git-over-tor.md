---
title: "Use Git over Tor"
date: 2016-10-29
slug: 2016-10-29-use-git-over-tor
type: posts
draft: false
categories:
  - default
tags:
  - tor
  - tutorial
---

*This post first appeared on my old blog in September 2016. It is preserved,
but maybe not updated, here.*

*Furthermore, It's December 2020 and I stopped running a public Gogs onion
service a long time ago. Maybe I'll do so again in the future, but for now,
keep in mind that this post references an onion service that doesn't exist.*

---

So you want to be a super l33t h4xx0r who stores his code on an onion service,
huh? Or maybe you want to anonymously obtain a copy of a project's source code.
Or you just think using Tor is cool. I'm with you there! Let's talk about how to
use Git over Tor. After we're done, you can create an account at my [Gogs onion
service](http://gogsys33repvmfz5.onion) and start hosting public or private
repositories on the "deep web!"

[[!toc levels=2]]


# Assumptions

- You're using Linux

  The instructions are almost exactly the same for macOS. Files may be in
  slightly different places or you may have to install programs a different way,
  but the gist is the same. There's probably a way to do this on Windows, but I
  don't use it.

- You're competent at using Linux

  In order to keep this general and useful to as many people as possible, I'm
  not going to hold your hand for every little step. I assume that you know how
  to use your distributions package manager to install a program or you can
  otherwise obtain and install a program. I assume you know how to start a
  system service. 

# Variables

So that this information can apply to as many people as possible, I have done my
best to not make any decisions for you.

## Tor or Tor Browser

Are you going to be using Tor or Tor Browser? It doesn't matter which you pick. You
might want to pick Tor if you want to be able to use Git at any time. You may
want Tor Browser if you can't install a system service, don't want
to, or only need Tor temporarily.

Later I will use `SocksPort` as a variable, which if you're using Tor, is 9050
by default. If you are using Tor Browser, then it is 9150 by default.

## HTTP(S) or SSH or Git

What protocol are you going to use as transport? If you don't know what that
means, then which of the three commands below do you expect to be using?

    # Git
    git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

    # HTTPS
    git clone https://git.torproject.org/tor.git

    # SSH
    git clone git@github.com:bitcoin/bitcoin.git

HTTP(S) is probably the most common. HTTP(S) and Git are the easiest to use, but
some places only allow pushing over SSH. I recommended you use SSH because you
can set it up such that its traffic goes over Tor transparently. You don't have
to change your behavior at all!

If you are going to be using HTTP(S) or Git as transport, then you must use
torsocks, as discussed later. If you use SSH as transport, you can use either
torsocks or netcat. I prefer netcat.

# 1. Obtain and start Tor

It doesn't matter how you do it. Install Tor and start it.

If you're using plain old Tor, start by looking in your package manager and
start it as a system service. If you're using Tor Browser, just decompress the
download and start the browser. Take note of the differences between the two in
the [variables section](#tor-or-the-tor-browser-bundle).

# 2. Obtain torsocks and/or netcat

Torsocks is a program that can transparently tunnel just about any program's
traffic through Tor. You will need it if you use HTTP(S) or Git as a transport.
You can use it if you want to use SSH as a transport.

Example clone with torsocks:

    torsocks git clone http://gogsys33repvmfz5.onion/mello/bm.git

If you are using SSH, I recommend you use netcat as once you're all set up, you
can `git clone` over Tor transparently.

Example clone with netcat:

    git clone git@gogsys33repvmfz5.onion/mello/bm.git

The complexity is hidden from you.

Not just any version of netcat will work. You need OpenBSD's netcat, not GNU's
netcat. How do you tell which one you have? Run `nc --help`. If the output
contains `[-X proxy_protocol]`, then you have the right version of netcat.

# 3. Configure torsocks and/or netcat

On my system, torsocks's config is located at `/etc/torsocks.conf`. If you are
using Tor (not Tor Browser), then you're done configuring torsocks. If you are using
Tor Browser, you need to edit torsocks's config to have `server_port = 9150` instead
of `server_port = 9050`.

If you're using netcat instead of torsocks, you needt to edit your user's SSH
config file. By default this is `~/.ssh/config`. Create the file if it doesn't
exist. Add the following to it.

    Host gogsys33repvmfz5.onion
        IdentityFile ~/.ssh/id_rsa
        ProxyCommand nc -X 5 -x localhost:SocksPort %h %p

Replace `gogsys33repvmfz5.onion` with the hostname of the website hosting your
code. Most places require you to identify yourself with a key instead of a
password, so change the path `~/.ssh/id_rsa` if needed. Finally, replace
`SocksPort` with `9050` or `9150` as discussed in [this
section](#tor-or-the-tor-browser-bundle).

# 4. Do it!

You've done everything now. You can now use Git over Tor. You've
downloaded/installed either Tor or Tor Browser, you've decided if
you want to use torsocks or netcat, and you've configured either torsocks or
SSH as needed. Let's test it out now. If you don't want to use my Gogs service,
then either ignore or modify the instructions below as you need.

These instructions assume you used netcat to transparently tunnel SSH traffic
over Tor for my Gogs service. If you didn't you need to use

    torsocks git VERB

instead of

    git VERB

where `VERB` is `clone`, `fetch`, `pull`, or `push`.

## Make an account

I recommend you make an account at my super cool Gogs onion service:
<http://gogsys33repvmfz5.onion>. If it asks for an email address when you
register, you should know that it doesn't have to be valid. You should also know
that while the website will complain if you don't have JavaScript enabled, it
will still __mostly__ work without it.

## Make a repository

After you have an account, make a repository. Once you've done that, you no
longer need to use the website for anything again until you want to make another
repository. Of course, you'll be missing out on cool features such as issue
tracking, pull requests, project wiki pages, and creating collaborative
organizations.

## Generate an SSH key

Instructions for how to do so are out of scope. There is plenty of information
on the Internet already.

After you have a key pair, upload the public key to Gogs here:
<http://gogsys33repvmfz5.onion/user/settings/ssh>

## Push your code

If you are starting a new project, you'll of course run something like the
following.

    mkdir my-repo
    cd my-repo
    git init
    git touch README.md
    git add README.md
    git commit -m "Initial commit"
    git remote add origin git@gogsys33repvmfz5.onion:test123/my-repo.git
    git push origin master

If you already have a project tracked by git, you'll want to run something like
the following to add Gogs as another remote.

    cd my-repo
    git remote add gogsys33 git@gogsys33repvmfz5.onion:test123/my-repo.git
    [ ... do programming, fix bugs, commit changes, etc. ... ]
    git push gogsys33 master


# Fun optional stuff

I don't like having to type out a long random onion domain. So since I use
netcat to tunnel SSH over Tor, my SSH config looks like this.

    Host gogsys33
        User git
	IdentityFile ~/.ssh/id_rsa
	ProxyCommand nc -X 5 -x localhost:SocksPort %h %p
	HostName gogsys33repvmfz5.onion

Notice that `Host` has changed and I've added a `HostName` and `User`. Now I can
transparently use Tor and also save on keystrokes. Some example commands:

    git clone gogsys33:mello/bm.git
    git fetch gogsys33
    git remote add gogsys33 gogsys33:mello/scripts.git

---

[[!tag tor tutorial]]
