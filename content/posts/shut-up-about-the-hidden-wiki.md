---
title: "Shut up about The Hidden Wiki"
date: 2019-11-11
slug: 2019-11-11-shut-up-about-the-hidden-wiki
type: posts
draft: false
categories:
  - default
tags:
  - onion-service
  - rant
  - thw
---

*This post first appeared on my old blog in November 2019. It is preserved, but
maybe not updated, here.*

---

The focus/organization of this post is poor and it does not contain much
technical information. You might want to skip this one.

[ddg]: https://duckduckgo.com
[ahmia]: http://msydqstlz2kzerdg.onion
[olsearch]: http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion
[tor66]: http://tor66sezptuu2nta.onion
[satpdf]: /papers/secdev19-satdomains.pdf
[zooko]: https://en.wikipedia.org/wiki/Zooko%27s_triangle
[gitea]: http://lgekyjf5vosmbfvcxzg3g5mmcncmwy4d3nhjrdqqiqzl5nmhqlfemaid.onion

I spent about an hour searching the web for the phrase "the hidden wiki" and
collected all the resulting websites I could find that called themselves that
or some slight variation of that. I searched using [DuckDuckGo][ddg],
[Ahamia][ahmia], something called [OnionLand Search][olsearch], and something
called [Tor66][tor66]*.

After deduplication, I found 48 websites, of which 46 were up right now. 40
sites were onion services.  **40 onion services** that you can easily find that
all call themselves the hidden wiki. When someone asks "hey, how do I find cool
onion services?" and you respond with "look up the hidden wiki," which one are
you talking about? Does it even matter? Do you even care that they will
probably type "the hidden wiki" into the URL bar of Tor Browser, which
defaults to searching with DuckDuckGo, which doesn't even index onion services,
so they're going to visit something like thehiddenwiki.org? Is that really what
you were intending?

Let's assume for a little bit that when you say "the hidden wiki," you're
talking about a specific one and you have the means to easily pull it up again.
It has also somehow established itself as trustworthy: it doesn't link to scams,
doesn't serve you malicious JavaScript, etc. Whatever. *How the hell is anyone
supposed to find it?*
The more-secure web comprised of onion services (colloquially and stupidly
referred to as "the deep web") does not yet have good search engines\*\*.
There's no good reputation tracking systems. The ones that exist look easily
gameable or malicious themselves. Good results don't just rise to the top.
Imposters don't get crowded out. **No one knows _which_ "hidden wiki" you're
talking about**. People lazily asking for links to interesting onion services
are annoying. People lazily throwing out "use the hidden wiki" and other
low-effort comments in response are just as bad.

<small>*If you recognize either of the latter two names, I am
not making any claim regarding the authenticity of the links I have for them;
the first two are the legitimate sites that go by those names.</small>

<small>**See rant at the end of this post.</small>

# Why so many?

I think it's all a bunch of people trying to piggyback off the popularity
of the name "The Hidden Wiki" in order to drive traffic to their site.
No doubt some of these people are acting with good intentions. Perhaps
they're carefully curating the links they allow onto their site. Maybe they're
simply providing a copy of this "valuable" information for a sense of pride.
Whatever. But I would bet money that many of these people have more malicious
intentions. For example: they've changed links such that they point to scams
that financially benefit them.

## Attack ... or mirrors?

While searching for these sites, I stumbled upon 10s of mirrors of the exact
same site (I collected ~10 but was looking at a wall of ~50).
I am familiar
with onion service operators trying to increase the
resiliency of their sites by running multiple onion addresses in parallel that
all point to the same site*. But I also suspect some operators will create tons
of copies of their site and submit them to search engines so that it is more
likely someone will stumble upon their site.

This person running 10s of mirrors of their site ... are they a good person
simply mirroring their site to try to make it more reachable? Is this a bad person
that has filled their site called "the hidden wiki" with a links to scams that
they operate? Is this just an amateur doing their best to attract traffic to
their hobby project that they believe is a good-faith effort of indexing safe,
legitimate onion services? **How would you know**?

<small>*I'm not saying this will work. Do it naively and you won't accomplish
anything.</small>

# Victims of success

Say you start a new website and host it at an onion service. You call it
something unique so it won't be confused with anything else (e.g. you don't
call your drug market "The Silk Road" and you don't call your link index "The
Hidden Wiki"). Your share your site and perhaps advertise it a bit. 
People start using it and you've reached some measurable level of success.

Due to the problems expressed thus far in this post, prepare yourself for
people to start impersonating *you*. I think you should especially expect this
if your site is financially successful or has the potential to influence where
people spend money.

This has happened recently. In the last year, a new index sprung up that
primarily lists currently working links for "known-good" drug markets. It's
popular with Redditors from what I've seen. People consider it trustworthy. But
search for it on DuckDuckGo, and the first result is not the original one.
In fact, the first 3 are all imposters, and the original is the 4th result.

# This is a hard, scientifically interesting problem

Smart people are actually trying to tackle problems like this. Here are some
things you might find interesting.

- [Zooko's triangle][zooko]
- [SAT domains][satpdf] (PDF) - written by Dr. Paul Syverson and myself
- PetNames
[[1](https://nakamotoinstitute.org/secure-property-titles/)]
[[2](http://www.erights.org/elib/capability/pnml.html)]
[[3](https://tools.ietf.org/html/rfc7700)]
- Cryptocurrencies such as [Namecoin](https://bit.namecoin.org/) and
  [Ethereum](https://ens.domains/) both support converting human-readable names
(e.g. alice.bit or bob.eth, respectively) to onion addresses. 
- [Part of Tor's work for Sponsor 27 work][s27] is a proof of concept for
  human-memorable addresses for onion services.

[s27]: https://trac.torproject.org/projects/tor/wiki/org/sponsors/Sponsor27

# A rant

I'm jaded. Put on your thick skin because this might hurt.

If suddenly you think making an onion service index or search engine sounds
like a fun little project: please don't. Please please please don't.  It won't
be very good, and that's only partly because there isn't much to find.
Something like
90% of the links you try will be dead
([§ 6.2](https://www.robgjansen.com/publications/torusage-imc2018.pdf)).
When you do find a
working site, you're going to ignore robots.txt and get stuck slowly
downloading all 30 translations of a website with 100 of thousands of links
that aren't interesting to anybody (*cough* the person crawling [my gitea
server][gitea]).  You're going to dump all this crap into a database, enable
full text search, and present search results to people with no discernible
order. If you add some sort of submission and/or ranking system, it's going to
be easily gameable. You think you implemented something that couldn't be gamed,
but it can.  You thought you would attract a community of people to help
moderate submissions, but none will come.  After all this hard work you'll
finally have something you can call "My First Search Engine" that you run for a
month before you get bored and move on. During that time all it ever
accomplished was abusively hammering the Tor HSDirs with lookups for onion
services that don't exist and forcing relays to perform the most expensive
crypto that they ever do in order to keep building circuits for you.

I've seen it so many times before. Please find a better fun project. It's cool
that you're excited about Tor. Put that energy into something else.
Hop on [Tor's IRC channel #tor](https://webchat.oftc.net/?channels=%23tor).
[Get involved](https://community.torproject.org/).
[Run a relay](https://community.torproject.org/relay/).
[Close a bug](https://trac.torproject.org/projects/tor).
Write a backpacking blog as an [onion service](https://community.torproject.org/onion-services/).
Host an IRC server or MUD as an onion service.  SSH into your home using an
onion service. Make some IOT devices talk to each other via onion services.
Anything is more productive than yet another crappy search engine.

I'm trying to speak from my experience here. I have a hard time finishing
projects. Some random person said in a comment (not even directed at me) that
constantly moving on to new projects is a sign of immaturity. While I'm not
sure I agree, it does make me think. I work on an idea because I think it will
be fun, and once it stops being fun I stop working on it.  But what I think
makes Yet Another Onion Service Search Engine different in my mind is that when
it stops being fun for you and you move on, you didn't just spend your own
time. You also put more load on the Tor network, and the Tor network is not
getting any bigger these days. People depend on it, and I don't think there's
as much capacity to spare as you might be led to believe from Tor Metrics.

I think people are going to disagree with me or at least disagree with the way
I've expressed my thoughts in this section. But I guess ... I guess maybe a
blog that's 100% technical 100% of the time isn't nearly as good. This at least
felt good to finally write down.
