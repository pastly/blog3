---
title: "Tracking Tor's network-wide V3 onion service outages"
date: 2021-01-13
slug: 2021-01-13-tracking-tors-v3-onion-outages
type: post
draft: false
toc: true
categories:
  - default
tags:
  - tor
  - onion-service
---

**Major update 28 Jan 2021 (UTC)**: It's happening again, but this time the
large amount of directory traffic is coming from exits.  We've missed three
consensuses, so v3 onions will be going down. Dirauths are already discussing
and trading patches to mitigate the issue in the short term.
The long-term solution for not
allowing people to use exits to do this is tracked [here][exit reentry].
Read the main body of this post for more information on, e.g., what a
"consensus" is and how not having them affects onion services.

[last year]: https://gitlab.torproject.org/tpo/core/tor/-/issues/33018
[actual fix]: https://gitlab.torproject.org/tpo/core/tor/-/issues/40239
[patch]: https://lists.torproject.org/pipermail/tor-talk/2021-January/045681.html
[bug]: https://gitlab.torproject.org/tpo/core/tor/-/issues/40237
[consensus health]: https://consensus-health.torproject.org/
[fallbacks 1]: https://lists.torproject.org/pipermail/tor-consensus-health/2021-January/011815.html
[fallbacks 2]: https://lists.torproject.org/pipermail/tor-consensus-health/2021-January/011840.html
[start of overload]: https://lists.torproject.org/pipermail/tor-relays/2021-January/019201.html
[recent consensus]: https://metrics.torproject.org/collector/recent/relay-descriptors/consensuses/
[archive consensus]: https://metrics.torproject.org/collector/archive/relay-descriptors/consensuses/
[alpha release]: https://blog.torproject.org/node/1969
[exit reentry]: https://gitlab.torproject.org/tpo/core/tor/-/issues/2667

It is January 13th, 2021 as I finish writing these initial words. Major updates may get
a date stamp next to them.

# Bottom line up front

- *Someone* is sending the directory authorities (and fallback dirs) lots of
  traffic.
- This causes the dirauths to no longer be able to reliably communicate.
- This means consensuses are no longer reliably produced every hour.
- No new consensus three hours in a row means new connections to v3 onion
  services stop working because of [a bug][bug].  Existing connections survive,
and no other part of Tor breaks at the three hour mark.
- There is an [alpha release][] for **experts who know what they are
  doing**.  It is making its way into all supported stable Tor versions.

Please keep these facts in mind:

- **It is unknown if the traffic hitting the dirauths is maliciously
  motivated**. People keep calling it an *attack*. I don't think we have the
evidence to back that up at this time.

- **There is no evidence that the traffic overload is actively trying to hurt
  v3 onions**.  A [similar situation existed last year][last year] and onions
didn't go down then. Claims that it is "the" government or rival drug markets
are not backed up with any evidence that I've seen.

If you have evidence of who is behind this traffic, please let someone know.
[Tor Project](https://support.torproject.org/get-in-touch/) or me
(blog comment, an email <small>(listed on [About
Me]({{< ref about >}}))</small>, or IRC message)

<small>While I currently work on Tor-related stuff for my job, nothing contained in this
post has anything to do with my work. Everything contained in this post is public unclassified
knowledge. Opinions expressed, if any, are my own.</small>




# Traffic starts hitting dirauths (again)

Roger points out on January 6th that
["the overload is back"][start of overload].

It's not OMGWTFBBQ levels of traffic. It's not from one IP nor is it from IPs
all over the Internet. One dirauth says it *seems* to be a poorly written
custom Tor client requesting directory information too often.



# Three missed consensuses

On January 9th, 10th, and 11th, there are repeated instances of 3 or more
consensuses in a row that are not generated.

This is the trigger for v3 onions no longer working. Consensuses are generated
every hour and are valid for 3 hours. Most parts of Tor (v2 onions, general
circuit building, etc.) do not require a *live* (currently valid) consensus,
but can get by just fine with a recently valid consensus (expired less than 24
hours ago). 

January 12th saw a few missed consensuses, but never 3 in a row. No consensus has been missed so far on the 13th.

# The bug and its fix

The v3 onion service code was written to require a live consensus, and it didn't need to be (devs
are verifying this). The [fix][patch] for this [bug][bug]
changes the requirement to just a recently valid consensus. It's getting tested
as I write these words on January 11th. The fix, or something very similar to
it, will be merged and backported in the coming days, at which point it's up to
the packagers for your OS or your tor-derived software (e.g. Tor Browser) to
notice the update and distribute it to you. I would expect Tor Browser to be updated very quickly.
Debian will probably take a day or two. Other distros, I have no idea.

If you're watching tor's logs, the current date includes "January" and "2021",
and you see the following message, then you have most likely hit the bug.

    Tried for 120 seconds to get a connection to [scrubbed]:6697. Giving up. (waiting for rendezvous desc)

The 6697 is *not* important. The "waiting for rendezvous desc" *is important*.

## Status of the fix making it into Tor

Primary sources for this section: [bug #40237][bug].

- Jan 12th: the fix is merged into 0.4.5.3-rc [[blog post](https://blog.torproject.org/node/1969)]

Upcoming events:

- backports to other supported versions of Tor
- packaging

# Fallback dirs getting hit too

On the 11th we
[notice][fallbacks 1]
the fallback dirs are also failing.
This is major evidence in my opinion that this is not a purposeful attack on the dirauths. I, and at least two dirauths, think it is most likely a bad custom Tor client implementation that requests directory information too often.

We see the same failing of fallback dirs [on the 12th][fallbacks 2].

[dirbytes now]: https://metrics.torproject.org/dirbytes.html?start=2020-12-01&end=2021-02-01
[dirbytes historic]: https://metrics.torproject.org/dirbytes.html?start=2019-10-01&end=2021-02-01

[This graph][dirbytes now] shows how the entire network is fielding more directory requests these days. [This graph][dirbytes historic] shows more context for where load usually is. The 1.5 Gbit/s the dirauths saw for ~half of 2020 is talked about in [this ticket][last year].

An actual attack could disguise itself like this, but if this were an attack, I would expect it to be more consistently effective at preventing consensus generation.

# It might be over now

*(Last updated 28 Jan 2021)*

The 14th saw no missing consensuses. If you had trouble reaching v3 onion services on the 14th, your issue is unrelated to the topic of this blog post.

The 15th saw no missing consensuses.

The 16th probably didn't miss any consensuses (I waited too long to check. Go look in [the archive][archive consensus] if you care enough).

The 17th saw none missing.

The 18th saw none missing.

So far the 19th saw none missing.

...

...

The 28th of January: lots of directory traffic at dirauths again. It is unknown
if fallback dirs see it too.

# FAQs

## What Tor relays/clients need to be updated?

No relays need to be updated. Tor clients hosting v3 onion services and Tor clients wishing to visit v3 onion services will need to be updated when the fix is released.

## How do I update my Tor?

*(Last updated 13 Jan 2021)*

You don't yet, unless you're willing to compile and use a version of Tor that isn't considered stable yet.
If you're willing, then see <https://blog.torproject.org/node/1969>.

## Should we temporarily downgrade to v2 while waiting for a fix?

If absolutely necessary, sure. Please keep in mind v2's issues (briefly described below in the glossary) and be aware that "temporary" probably means ~1 week (*crossing my fingers*). I personally will just suffer and wait for the fix to be released.

## Are v3 onion services fundamentally broken?

No.

## Is this really major?

Eh ... yes because of the impact, but no because the fix is easy and will be out quickly.

## Who was it?

[torpy thread]: https://lists.torproject.org/pipermail/tor-dev/2021-January/014504.html
[torpy thread roger]: https://lists.torproject.org/pipermail/tor-dev/2021-January/014510.html

One possibility is people using some 3rd party Tor client called "torpy." See the 5+ messages in [this tor-dev@ thread][torpy thread], especially Sebastian and [Roger's][torpy thread roger] responses.

# Glossary and preemptive rebuttals

## Directory authorities / dirauths

There are 9 relays operated by highly trusted individuals that decide the state
of the network. They decide what relays are a part of the network and what
certain network parameters should be set to.

In a way they are a "single" point of failure and make the Tor network
"centralized." Decentralizing their role to 100s, 1000s, or every relay would:

1. require massive fundamental changes to how Tor works. By itself this
   probably is not a convincing reason to not do it.

2. open Tor up to new attacks it currently isn't vulnerable to. This should be
   a bit more convincing. The keyword to Google for most of them is "Sybil".

Having a "single" high quality root of trust is a valuable property that
"decentralize all the things!" people do not generally appreciate enough, in my
opinion.

You: *This v3 onion fix doesn't actually address the root problem: the dirauths weren't
able to communicate and create consensuses.*

Yes! You are absolutely right that *something* about how the dirauths work should
change such that they can continue communicating with each other even in the
presence of malicious (purposefully malicious or not) traffic!
[This ticket][actual fix] is one idea and a good place to start your research
if I say nothing more and you want to research what is being done yourself.
They might also update [this ticket][last year].

## V3 onion service

The new type of onion service. Names are 56 characters long, like 
tv54samlti22655ohq3oaswm64cwf7ulp6wzkjcvdla2hagqcu7uokid.onion. V2 onions are
16 characters long, like 3g2upl4pq6kufc4m.onion.

V2 onion services use old crypto and old protocols that are obsolete and
dangerous *now* or will be soon. The code for v2 is messy and the protocol is
not extensible. V2 onions are vulnerable to harvesting by malicious HSDirs, and these malicious HSDirs exist today (and are removed as soon as they are detected).
Support for v2 onion services will be removed from Tor soon. V3 onions are the
future despite the current events.


##  Fallback directory mirror / fallback dir

Tor clients don't usually *directly* fetch consensus information from a dirauth
anymore. There's too many people using Tor and only 9 dirauths. Instead, a
large number of relays that are high quality have opted in to also be hardcoded
into Tor source code so clients can usually fetch consensus data from them on
first run. After first run and successful connection to Tor, clients get this
stuff from their guard instead.

## Consensus

The dirauths vote on what relays are currently in the network and what certain network
parameters should be set to. The "average" of their votes become the consensus.
They make a consensus every hour and each is valid for three hours. Clients typically
fetch a new consensus every two hours.

You can see information from the current consensus [here][consensus health]. Recent consensuses
are archived [here][recent consensus]
and older ones archived [here][archive consensus].
