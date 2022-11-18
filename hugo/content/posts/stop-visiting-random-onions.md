---
title: "Stop Visiting Randomly-Generated Onion Services"
date: 2019-01-24
slug: 2019-01-24-stop-visiting-random-onions
type: posts
draft: false
categories:
  - default
tags:
  - onion-service
  - rant
  - tor
---

*This post first appeared on my old blog in January 2019. It is preserved, but
maybe not updated, here.*

---

If you've written a script that tries to access random onion services, or all
onion services in order, or something else that attempts to brute force the
namespace of onion services ...

You don't realize how unlikely it is that you will ever find a working link.

- There's about [100,000 v2 onion services that are running right now](https://metrics.torproject.org/hidserv-dir-onions-seen.html) (as of Jan 2019)
- Of those, an unknown fraction are listening on port 80/443 (web sites). The number seems to be no more than 10,000 based on other peoples' attempts at indexing onion services, but let's assume it's all 100,000.
- There's 1,208,925,819,614,629,174,706,176 possible v2 onion services
- Thus there's an 100,000 / 1,208,925... == 8.27*10^(-18)% chance that any v2 onion service you generate will be up and responding. AKA a 0.00000000000000000827% chance.

Let's put that tiny number in some context. How about Powerball?

- The [odds of winning the Powerball jackpot is 1 in 292,201,338](https://www.powerball.com/games/powerball) (3.42*10^(-7)%)
- This means you are approximately 100,000,000,000 times more likely to win the next Powerball jackpot than the next random v2 onion service you click on/generate/whatever actually being up and responding
- Said another way, if you could check 100 billion v2 onion services by the time there's another Powerball drawing (say ... in a week), you have an equal chance of finding **one** working v2 onion address as you have of winning the Powerball jackpot. This means checking 165,343.9 onion services **per second, every second** for the next week in order to have a 1 in 292 million chance that **one** of them is up and responding.

[list]: {{< ref "stop-visiting-random-onions" >}}

You will never find a working onion service by randomly clicking on links on
[my list of all onion services][list] or by randomly
generating links and trying them.

By trying you are wasting Tor network resources. This isn't a problem if you
are a human just clicking on a few links in my list of all onion services. But
if you write a script that does this, you start having a significant effect.
You are making a bunch of Tor relays waste resources building circuits for you
to look up onion service descriptors that don't exist. That's not exactly
cheap. Circuit building is some of the most expensive crypto Tor has to do.
This is a waste of electricity and a waste of the limited valuable resource of
Tor network capacity, which [some people actually rely
on](https://www.torproject.org/about/torusers.html.en) to live a free life.

(Oh and there's even more possible v3 onion services)
