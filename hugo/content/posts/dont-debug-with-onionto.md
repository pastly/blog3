---
title: "Don't Debug with Onion.to"
date: 2016-12-02
slug: 2021-12-02-dont-debug-with-onionto
type: posts
draft: false
toc: true
categories:
  - default
tags:
  - tor
  - tor2web
  - tor-browser
---

*This post first appeared on my old blog in December 2016. It is preserved, but
maybe not updated, here.*

---

This also applies to onion.cab onion.city, onion.direct, and any onion domain
that does not end in exactly
`.onion`. These are called Tor2Web proxies and they can be very dangerous if
you don't know how they work.

__Update 4 (June 2019)__:

- [Many Tor2Web proxies are doing the malicious things I talk about in this post][medium1]
([archive](https://archive.fo/hMN8X))
- I've seen Tor2Web proxies that seem to have manually added v3 onion support
  for themselves (since, as far as I know, Tor Project hasn't done it and won't
do it). I can't name any.
- There's nothing special about the word "onion" in the domains these Tor2Web
  proxies often use. "Onion" only makes using them a little easier as the user
merely needs to add ".to" or similar to the end. darknet.to is apparently a
Tor2Web proxy, as is/was tor2web.org and s1.tor-gateways.de.
[Random Reddit user as source][reddit2].

__Update 3__: Tor 0.3.2.9 was the first stable version that ended up having
support for v3 onion services.

__Update 2__: Tor 0.3.1.x (stable release scheduled for late 2017) adds the
"next generation of onion services." This new type of onion service [will _not
even work_](https://trac.torproject.org/projects/tor/ticket/21593#comment:1)
with Tor2Web proxies. If you're reading this far in the future (late 2017 or
later) and you're visiting an onion domain that's really long (50+ characters
instead of only 16) then keep in mind that this post only applies to the current
type of onion services with short addresses.

__Update 1__: due to some confusion [on Reddit][reddit1], here's some explicit
examples.

`<anything>.onion.link/blah.php` is bad because it's going through a Tor2Web
proxy  
`<anything>.onion/blah.php` is good because it isn't. It's normal. Use this.

# Why they exist

They exist so people can access onion services without using Tor. That's it. If
the user doesn't know all the caveats that come along with that benefit, then
she is probably really hurting herself. And if the user is already using Tor
Browser, there is no valid reason for her to be using a Tor2Web proxy. __Tor2Web
proxies are not a troubleshooting step__. Please stop using them like one.
Please stop suggesting them to people.

# Why they are bad

## Payload/Session Leakage

Since the Tor2Web proxy is the one connecting to the onion service for Alice, it
gets to see everything. If Alice is visiting a forum or image board, the proxy
gets to see all the posts and all the images. If Alice is logging into
something, the proxy gets to see her credentials.

Let me repeat that. __When you use a Tor2Web proxy, it gets to see EVERYTHING.
Your credentials if you sign in. Any cookies. Any uploads you make. All the
pages you request and their contents.__

Not only can it **see** everything you do, it can change anything it wants. It
can replace all pictures with cats. It can replace all bitcoin addresses with
ones that it owns. It can add its own JavaScript and advertisements.
[Many already do this][medium1].

## Onion Service Enumeration

Tor2Web websites are like regular websites. Like google.com or facebook.com.
When the browser gets a request for anything.onion.to, it consults DNS to
resolve it. So every DNS server that the computer is configured to talk to (and
is told to forward its request onto by its configured servers) will find out
that anything.onion exists and someone wants to access it. If the user, Alice,
isn't using Tor Browser, then the DNS servers also find out that the someone is
her. Not good!

Even if Alice is using Tor Browser, now the Tor2Web proxy knows that
anything.onion exists. In fact, many have sold or still sell information on what
onion services have been requested through them. For example, see [onion.cab's
list](https://onion.cab/list.php).

## User/Onion Correlation

This is very similar to a point made already, but this focuses on the
consequences to the user.

The Tor2Web proxy knows someone is interested in anything.onion. If the user
isn't using Tor Browser, the Tor2Web proxy also knows the IP of the user. If
that's not bad enough, if for some reason the Tor2Web proxy suspects that this
anything.onion is (almost) never accessed by anyone else, then it may conclude
that the person that just requested the onion service must be the
owner.

# Real Troubleshooting

If anything.onion doesn't work for you, _don't go and try anything.onion.to_.

If you are using Tor Browser, and have changed network proxy settings like you
would in regular Firefox, __don't do that__! You are probably able to connect to
regular websites and anything.onion.to, but you won't be able to connect to
anything.onion because __you aren't using Tor__. You are not being secured by
Tor. The only way you should change
proxy settings is via the onion button, and you should only do that if your ISP
requires it.

If you are using Tor Browser, you didn't change proxy settings, you can access
anything.onion.to, you can't access anything.onion, and you're pretty sure
Tor/Tor Browser are working fine, then __the onion service is probably down__.
There's nothing you can do about it. The anything.onion.to is just a cached
copy of parts of the onion service that the Tor2Web proxy has fetched recently.
You aren't getting the real website and you can't interact with it. Poor uptime
is a fact of life for most onion services. They are often short-lived, are only
up a few hours each day, or both. Most are run by amateurs.

# Summary

Don't play with your anonymity. Learn a little bit about how things work so you
can be safe. Adding something to the end of an onion address sounds like a good
easy way to get access to something that isn't working, but it isn't.
Slightly changing youtube.com into some other domain name that fetches the video
for you so you don't have to sign in to watch something flagged as adult is the
same idea, but at least your safety (probably) isn't at risk in that case.

[reddit1]: https://www.reddit.com/r/onions/comments/5nyp19/reminder_to_not_use_tor2web_proxies_like/dclbcgo/
[medium1]: https://medium.com/@c5/tor2web-proxies-are-using-google-analytics-to-secretly-track-users-fd245dbc81c5
[reddit2]: https://redd.it/bx19c6
