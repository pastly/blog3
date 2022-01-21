---
title: "Creating Private Onion Services"
date: 2017-02-25
slug: 2017-02-25-creating-private-onion-services"
type: posts
draft: false
categories:
  - default
tags:
  - onion-service
  - tutorial
  - tor
---

*This post first appeared on my old blog in February 2017. It is preserved, but
maybe not updated, here.*

---

**January 2019 Update**: This post applies to v2 onion services that are 16
characters long such as
[mattttttssi4lhud.onion](http://mattttttssi4lhud.onion/).
In January 2019, Tor 0.3.5.7 was released as the first stable release of the
0.3.5 series. Among other things, it is the first stable release of Tor that
supports client authorization of v3 onion services
(like [zfob4nth675763zthpij33iq4pz5q4qthr3gydih4qbdiwtypr2e3bqd.onion](http://zfob4nth675763zthpij33iq4pz5q4qthr3gydih4qbdiwtypr2e3bqd.onion/)).
This post that you are currently reading walks you through client authorization
for v2 onion services. See [[this post|creating-private-v3-FgbdRTFr]] for
a walk through of client authorization for v3 onion services instead.

[tor-man]: https://www.torproject.org/docs/tor-manual.html
[tor-hs]: https://www.torproject.org/docs/tor-hidden-service.html.en
[rend-spec]: https://gitweb.torproject.org/torspec.git/tree/rend-spec.txt
[ticket]: https://bugs.torproject.org/19757
[basic-issue]: https://bugs.torproject.org/14854

You're probably aware of many of the great features of onion services.

- end-to-end encryption
- location hiding
- assurance you're talking to the server you think you are
- firewall traversal

You may have ever heard about how misbehaving relays with the HSDir flag can
learn the existence of onion services _that their owners literally never
advertised anywhere_. This attack and related attacks will be impossible when
the next generation of onion services is deployed (see end of this post for more
information), but did you know can prevent this from happening right now, today,
on your onion services?

This is thanks to a feature of Tor onion services that can _prevent anyone from
even connecting to your service if they don't have your permission_. I'm not
talking about a login page on example.onion, I'm talking about the inability
for random people to be able to tell that example.onion is up __or if it even
exists__.

I'm talking about the HiddenServiceAuthorizeClient (server-side) and HidServAuth
(client-side) torrc options that you can find in the [Tor manual][tor-man].

There are two ways to use this: basic and stealth. The gist with both is

- the server tells its Tor process to generate some tokens
- the server operator gives a token to each user he wants to allow to access his
  onion service
- the users tell their Tor processes about their token and then they can connect

After this setup is done, clients authenticate automatically with no further
work from the user necessary.

__Basic__

- up to about 50* different tokens (users) can be specified
- all users connect to the same .onion address
- HSDirs know the onion service exists (but they can't connect as they don't
  have a token)

\* The [spec][rend-spec] says up to 512, but there seems to be an
[issue][basic-issue] specifying more than 49 or 50.

__Stealth__

- up to 16 different tokens (users) can be specified
- each user connects to a different .onion address
- HSDirs do __not__ know the onion service exists (and even if they did, they
  still can't connect as they don't have a token)

I'm going to assume you--the onion service operator--already have your onion
service up and running. Or you at least know the basics on how to. [See
here][tor-hs] for help if you don't.

So we know creating an regular onion service is as easy as adding two lines to
the torrc. Something like the following will tell Tor to create two onion
services.

    HiddenServiceDir /usr/local/var/lib/tor/foo_service/
    HiddenServicePort 12623
    
    HiddenServiceDir /usr/local/var/lib/tor/bar_service/
    HiddenServicePort 54829

Let's make `foo_service` use basic client authorization, and `bar_service` use
stealth client authorization. Let's also give three people access to each.

    HiddenServiceDir /usr/local/var/lib/tor/foo_service/
    HiddenServiceAuthorizeClient basic Alice,Bob,Charlie
    HiddenServicePort 12623
    
    HiddenServiceDir /usr/local/var/lib/tor/bar_service/
    HiddenServiceAuthorizeClient stealth David,Earl,Fred
    HiddenServicePort 54829

After reloading Tor, each service's directory will now exist and contain three
files: `client_keys`, `hostname`, and `private_key`. Feel free to look, but the
only one we need is `hostname`. You might be used to it only containing a single
line with a single onion address on it, but that's not the case anymore. For
example, let's look at the contents of mine.

__`foo_service/hostname`__

    bcxmhwc2iqcrcknh.onion n62CiiB2LC9vjlwNm2iwEw # client: Alice
    bcxmhwc2iqcrcknh.onion QyfrjJhHuVj0uR+X6BK61w # client: Bob
    bcxmhwc2iqcrcknh.onion Z/ghYM8WG0eXYp9MvYntcw # client: Charlie

__`bar_service/hostname`__

    ovxfhd37q7ntkobe.onion 2owiKJaf2RSIFpCxMIcZMh # client: David
    m324vced6pkv5tdx.onion VUXx3piRLBPGUnBbVt93zR # client: Earl
    34dxzb72fbewytse.onion 5FLhOZdz3elEMbqjdnAIQB # client: Fred

Now you, dear onion service operator, just need to give Alice's line to Alice,
Bob's line to Bob, and so on.

And you, Ms. Alice, should find and edit your torrc to include the following
line once you get it from the operator.

    HidServAuth bcxmhwc2iqcrcknh.onion n62CiiB2LC9vjlwNm2iwEw auth-for-foo

(Where `auth-for-foo` is optional and anything you want it to be in order to
help you remember what this line is for)

If you're interested in the nitty gritty details about how basic/stealth client
authorization works, checkout section 2 of the [specification][rend-spec].

If you think it would be nice for Tor Browser to add an easy way for users to
add `HidServAuth` lines, [you're not the first][ticket]. In the mean time, you
need to find Tor Browser's torrc and add it yourself.

On Linux, you extracted Tor Browser somewhere when you installed it. Within that
directory, the torrc is at `Browser/TorBrowser/Data/Tor/torrc`.

On OS X, it will be at a similar path in
`/Users/<yourname>/Library/Application Support/TorBrowser-Data`.

On Windows, it will be at a similar path in the Tor Browser directory on your
desktop.

---

More info on the next generation of onion services:

- <https://blog.torproject.org/blog/hidden-service-hackfest-arlington-accords>
- <https://blog.torproject.org/blog/mission-montreal-building-next-generation-onion-services>
- <https://gitweb.torproject.org/torspec.git/tree/proposals/224-rend-spec-ng.txt>
- <https://trac.torproject.org/projects/tor/ticket/12424>
