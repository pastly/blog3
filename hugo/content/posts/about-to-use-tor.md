---
title: "About to use Tor. Any security tips?"
date: 2019-01-19
slug: 2019-01-19-about-to-use-tor"
type: post
draft: false
toc: true
categories:
  - default
tags:
  - tor
  - tor-browser
---

*This post first appeared on my old blog in January 2019. It is preserved, but
maybe not updated, here.*

---

If you're going to browse the web, use Tor Browser. Don't try to make Firefox,
Chrome, or something else proxy its traffic over Tor. There is no combination
of settings tweaks that produces as good of a product as Tor Browser. You will
be essentially uniquely fingerprintable. You will not get Tor Browser's awesome
state and traffic isolation.

The rest of this post assumes you want to browse the web.

Read Tor's suggestions on their
[download page](https://www.torproject.org/download/download-easy.html.en#warning).

**This is where most people should stop giving concrete advice without knowing
your adversary model. Nonetheless they keep going and suggest ...**

# Adding a VPN

[vpn-plus-tor]: {{< ref "vpn-tor-not-net-gain" >}}

It sounds good, but it only helps in a small number of cases, [does nothing in
most cases, and hurts in a small number of cases][vpn-plus-tor].

If you're going to say something about

- hiding the fact you use Tor from your ISP
- adding extra hops
- but VPNs don't log
- Five eyes / geolocation

then read my blog post (linked above) first please.

# Disabling JavaScript / setting the security slider to its highest setting

This is unnecessary for the majority of adversary models and will make the web
significantly less usable.

The only people who have had significant JavaScript exploits used against them
in Tor Browser were pedophiles using Windows. This suggests to me (and security
experts in general, AKA not people that read "tech news" and parrot everything
they read) that these exploits are rare, expensive, and hard to replace. Thus
they aren't going to be used against random people because the risk of the
exploit being discovered and fixed is too great.

Setting the security slider to its highest setting does remove JavaScript as a
possible attack vector. So as long as you set it there consciously, are aware
much of the web may break, I support your choice to disable it. I especially
support it if you have legitimate concerns that JavaScript exploits may be used
against you, not just dumb paranoia.

# Using Tails or Whonix

Tails is overkill for the majority of adversary models. Tails is awesome
though, for when you do actually need it.

I neither suggest for or against using Whonix.

# Not logging in to "real" accounts over Tor

There's generally nothing wrong with logging in to "real" accounts over Tor.

Tor Browser intelligently isolates your traffic so logging in to your "real"
Facebook while doing secret stuff on a different website is not correlate-able
via traffic patterns. 

It also isolates local state (like cookies) so it won't leak that way.

Finally, most sites worth using and logging in to these days use HTTPS, making
it
[impossible for exits to steal your credentials](https://www.eff.org/pages/tor-and-https)
(and when they try, they get noticed by people monitoring the network for
malicious relays and removed from the network).

Some places (especially banks) will treat you poorly if you visit them over
Tor.  I've heard that banks will generally lock your account until you contact
them. But this is different than having security issues introduced, which is
usually what people are thinking about when giving this advice.

# Testing your fingerprint

With websites such as
[panopticlick](https://panopticlick.eff.org/),
[Fingerprint Central](https://fpcentral.tbb.torproject.org/) (beta, operated by Tor Project),
[BrowserLeaks](https://browserleaks.com/), or
[TorZillaPrint](https://arkenfox.github.io/TZP/tzp.html)
to see how anonymous you are.

If the site you use doesn't give you an "anonymity score" but just gives
you a bunch of numbers and information you don't understand, don't read into
it. Don't immediately assume that just because there is information being
displayed to you that that information is identifying. Do some research
(posting on Reddit as your first step is more similar to spreading FUD than
research, so do that last please) and try to determine if the scary looking
info is actually not scary at all.

If the site does give you an "anonymity score," did you get a good result or a
bad one?  How do you know? If the fingerprint-testing site determines your
score based on its recent visitors (like panopticlick), are their recent
visitors a representative sample of the visitors of the other websites you
visit? If yes, how do you know?

What are the features the fingerprint-testing site tested for and how does that
set of features compare to the ones that other websites look for? If you claim
they are similar, how do you know?

If you test your browser, make a change to it, test again, and then get the
same score, is it really safe to assume that the change was benign? If you get
a better score, is that meaningful? What if the score got worse?

If the fingerprint-testing site relies on JavaScript for the detection of many
features (and they generally do), is JavaScript the only way to detect those
features? It often isn't. If you disable JavaScript and get a much better
score, is that actually meaningful? Why or why not?

**See how much uncertainty I have about fingerprint-testing websites**? I find
it mind boggling that people who don't really understand what they're looking
at try to claim anything concrete after using one of these sites, *especially*
after using ones that give them an "anonymity score."

[you-want-tor]: {{< ref "you-want-tor-browser-not-a-vpn" >}}

[This post][you-want-tor] in the "Untruth: VPNs
prevent tracking [...]" section has a **non-exhaustive** list of **some** of
the things that may be used to track you, many of which fingerprint-testing
sites don't even consider.

Finally, Tor Browser tries to make you look like as many other Tor Browser
users as possible, not like as many other people as possible. For example,
hardly any Internet user has their browser open to exactly 1000x1000, but of
those that do, they are all very similar because essentially all of them are
using Tor Browser.

Please don't freak out over your vanilla Tor Browser "failing" a fingerprint
test. It probably hasn't. Please do some research to see if your result is good
or bad before running to Reddit.

# Adding extra extensions to Tor Browser

Such as privacy badger or uBlock origin.

Privacy badger is either pointless (because bad ads and tracking scripts aren't
going to be able to track you while you use Tor Browser anyway) or harmful (its
blocking behavior is based on your behavior, so the pattern with which your
browser is blocking stuff becomes more identifying to you).

uBlock origin is great for blocking ads and making the web faster. I use it in
Firefox and most of the time in Tor Browser. However, using it will add to your
fingerprint because now you are blocking ads ... unlike most Tor Browser users.
Tails does include uBlock origin by default, but you will not be able to blend
in with this group of people unless you are also using Tails. If you are fine
with being more easily fingerprintable<sup>*</sup>, then perhaps uBlock origin
is fine.

<sup>*</sup> Someone contacted me because they have actually tested how unique
they were according to Panoptclick with and without uBlock (origin?). They saw
with a default TB that 1/5000 have the same fingerprint as them, a relatively
good result. With default TB and uBlock (origin?) they were unique in a pool of
200,000 people, a pretty bad result. This is a pretty big difference, and
despite not knowing very much about their test setup and what else went into
the results they saw, I must acknowledge that uBlock (origin?) makes you more
than "slightly more fingerprintable", which was my previous claim. Thank you
for reaching out. **edit**: the same person updated me to say that they ran the
tests again, but with a very controlled setup. With both the original version
of TB and the updated one that had been released, **now** they got exactly the
same ~1/5000 (AKA good) result regardless of whether or not uBlock origin is
installed. What changed? What happened? They don't know, and neither do I. So
I point the reader back at the
[Testing your fingerprint](#testing-your-fingerprint) section for why I don't
think you should care very much about what a fingerprint test site tells you.
