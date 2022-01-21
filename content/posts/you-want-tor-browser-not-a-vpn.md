---
title: "You want Tor Browser ... not a VPN"
date: 2019-10-17
slug: 2019-10-17-you-want-tor-browser-not-a-vpn
type: posts
draft: false
categories:
  - default
tags:
  - tor
  - tor-browser
  - vpn
---

*This post first appeared on my old blog in October 2019. It is preserved, but
maybe not updated, here.*

---

In most cases.

[tls-web-traffic]: https://transparencyreport.google.com/https/overview
[bad-relays]: https://trac.torproject.org/projects/tor/wiki/doc/ReportingBadRelays
[about-me]: /posts/2016-08-28-about-me/
[fullscreen-browser]: https://old.reddit.com/r/TOR/comments/czftid/not_setting_browser_window_to_fullscreen/eyykf6p/
[mouse-movement]: https://www.businessinsider.com/websites-apps-track-mouse-movements-screen-swipes-security-behavioral-biometrics-2019-7
[fb-shadow]: https://www.theverge.com/2018/4/11/17225482/facebook-shadow-profiles-zuckerberg-congress-data-privacy
[hsts-tracking]: /papers/foci18-paper-syverson.pdf
[alt-svc-pdf]: /papers/hotpets19-pushing-security.pdf
[alt-svc-pptx]: /papers/hotpets19-pushing-security.pptx
[apple-hsts]: https://webkit.org/blog/8146/protecting-against-hsts-abuse/
[hsts]: https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
[alt-svc]: https://tools.ietf.org/html/rfc7838
[audio-fp]: https://audiofingerprint.openwpm.com/
[canvas-fp]: https://browserleaks.com/canvas
[tb-design]: https://2019.www.torproject.org/projects/torbrowser/design/
[torrent-over-tor]: https://blog.torproject.org/bittorrent-over-tor-isnt-good-idea
[tor-users]: https://2019.www.torproject.org/about/torusers.html.en
[relay-flags]: https://metrics.torproject.org/relayflags.html
[deepweb-size]: https://old.reddit.com/r/TOR/comments/bjo481/isp_and_law_enforcement_can_quite_easily_find_out/emburh9/
[what-deepweb]: https://old.reddit.com/r/TOR/comments/cvpbla/why_the_deep_or_dark_web_as_popularly_depicted/

[[!toc levels=2]]

# Untruth: VPNs protect you from local network hackers

This is usually claimed in the context of open WiFi networks such as those at
airports or coffee shops, and is basically correct. As long as you have a
reputable VPN company and they set up their software correctly, then VPNs help.

A little.

Today, [well over 2/3 of web traffic being protected by TLS][tls-web-traffic]
and all (not scientifically determined, just a baseless claim by me) of sites
worth using have and force HTTPS on clients. TLS and the CA system has its
issues, but your average little coffee shop hacker is not going to be able to
attack it nor convince your browser to downgrade to clear text, so you were
already fine. All this hacker is going to learn is the sites that you are
visiting: not your account name, not your password, and not what you do on that
site.

Claims that VPNs protect your passwords or bank accounts or that they add any
meaningful amount of security/privacy/anonymity in this context inside your
home are bullshit.

## VPN vs Tor Browser

In this context, since the VPN wasn't doing much of anything to begin with,
they are essentially the same. Tor (thus Tor Browser) is in fact built
correctly to disallow anyone from ever intercepting and reading the traffic
between you and your guard relay. If your chosen VPN isn't (good luck figuring
it out), then Tor (Browser) is better. But honestly, your VPN is probably just
as good.

# Untruth: VPNs protect you from getting malware

See previous section's claim about hackers not being able to attack TLS. They
aren't going to be able to inject anything into the content you're downloading.

If you believe *your* adversary can attack TLS, then I argue it is foolish to
believe your adversary is only capable of existing on the protected link
between you and your VPN and is unable to exist on the unprotected link between
the VPN and your ultimate destination. This is a strong adversary and they
probably have a sufficiently global presence to attack you.

The above is the only way I can see how this claim *might* make sense. VPNs do
nothing to prevent you from accidentally visiting malicious sites. Claims that
they do are bullshit.

**Update Oct 2019**: I've been informed that a couple VPN providers offer to
spy on your traffic and block it if they deem it to be dangerous. If their
users trust them and the companies continue to behave well while exercising
this power, then I see this as a net value gain. Not all VPNs have this spying
feature. I argue that using uBlock Origin in your browser (assuming your
adversary model allows you to do so) probably accomplishes just as much
protection (and it's free).

## VPN vs Tor Browser

In this context, VPNs and Tor (Browser) as essentially the same. However, Tor
(Browser) has some nice added benefits.

People love to point out how Tor exit relays are in a position to attack your
traffic. This is a true statement. However, this is a true statement too: VPNs
are in a position to attack your traffic. In fact, VPNs can attack your traffic
in a *targeted* manner. VPNs know who you are, exits don't. VPNs can choose to
only do bad things to *your* traffic, exits can't. This is great if they want
to avoid detection.

Speaking of detection, when Tor exit nodes get caught misbehaving or attacking
users, they get [reported and removed from the network][bad-relays]. Tor
Project runs automated scans constantly to detect the most common types of
malicious activity.  Since the exits can't differentiate between a regular user
and this scan, they're going to get caught.

# Untruth: VPNs prevent tracking done by websites and big Internet companies

Ha. No.

Yes, they change your IP as it appears to the websites that you visit. There is
a hell of a lot more to being anonymous or preventing tracking than your IP address.

First of all, perhaps the VPN gives you an IP address that no one else is
using. Or perhaps you are tech savvy and set up your own private VPN server on
a VPS for yourself. Cool. Now *that* IP address identifies you instead of your
home one. You gained basically nothing.

But that's not generally how it works. Generally you appear to have an IP
address that many of the VPN's other customers are using at the same time as
you. Now you're in a pool of users, so now you can't be tracked, right? Wrong.

There is *so much* that websites and big Internet companies (e.g. Facebook,
Google) are doing or can do to track us that do not rely on IP addresses.
It's not funny. It's serious. It should stop. We should fight it.

**They**/**them** is used liberally to mean "that relevant big Internet company(s)."
**Do** means there's evidence of at least one of them doing something.
**Can** means its technically possible, maybe they're doing it, but I don't
actually know. Not all bullets are possible in all browsers, nor am I claiming
there is zero ways to combat each bullet.

- They **do** give you cookies. Obviously. Cookies are going to allow them to
  track you regardless of how often you change your IP address or how super
mega awesome anonymous you believe yours is. Browsers are getting better at
preventing this type of tracking.

- They **can** [[detect the size of your browser window|how-css-alone-can-help-track-you-YF4ciVY6]] even without
the help of big bad JavaScript. Your window is probably a different size from
everyone else using your VPN with your shared IP address right now. No,
[maximizing your browser or having a common monitor resolution doesn't help][fullscreen-browser].

- They **can**/**do** detect a wide variety of other features of your browser,
  including but not limited to your user agent, your supported fonts, the way
your browser renders [graphics][canvas-fp]/[audio][audio-fp]. your date, time
and timezone, which ads you load if any, and which scripts you load if any.

- They **do** [track your mouse movements and other "behavior biometrics"][mouse-movement].

- They **do** [track you even if you don't have an account on their site][fb-shadow].

- They **can** abuse good web security protcols such as [HSTS][hsts]
  ([PDF][hsts-tracking]) to track you. [Apple found evidence of
**do**][apple-hsts]. 

- They **can** abuse web protocols such as [HTTP Alternative Services][alt-svc]
  ([PDF][alt-svc-pdf], [PPTX][alt-svc-pptx]) to track you. I've heard from a
reliabe source that one big Internet company is **do**ing so, but cannot cite
this information. Feel free to not trust me.

Whew let's stop there. That's a lot of stuff. How do VPNs and Tor Browser compare?

## VPN vs Tor Browser

- Tor Browser has intelligent first-party isolation of local state (i.e.
  cookies but other stuff too) so that state you get while logged in to
facebook.com in tabs 1, 2, and 3 is not accessible from tabs 4 and 5 where you
are browsing nytimes.com. Cookies cannot track Tor Browser users across sites.
VPNs do nothing in this space.

   - Side note: Tor Browser also intelligently isolates your traffic. With VPNs
     all of everything exits from the same IP address. With Tor Browser, all
traffic from facebook.com tabs **regardless of the destination domain of the
requests** uses one set of circuits through the Tor network while all traffic
from nytimes.com uses a different set of circuits. Even if all the sites you
visit use the same CDN for serving their images/videos/ads, neither the sites
nor the CDN will be able to tell that it's you that is visiting facebook and
nytimes at the same time.

- Tor Browser defaults to the same window size for all users (1000x1000 if
  possible, but in increments of 100x100 if the former can't fit on your
display). Window size cannot be used to track Tor Browser users. VPNs do
nothing in this space.

- Tor Browser takes additional measures to make all of its users have as
  similar of a browser fingerprint as possible. All users have the same
supported fonts.  Graphic/audio fingerprinting is mitigated. All users have the
same timezone. All users load ads and scripts by default. WebRTC is not supported.
VPNs do nothing in this space.

    - For users who do not wish to load scripts or in general desire higher
      levels of security, an easy-to-use security slider is provided for them
in Tor Browser.  When many people use the slider, it allows them to achieve
this higher security without having to manually change browser settings and
potentially stand out as having done so slightly differently from other people.

- Tor Browser attempts to mitigate behavior-based tracking. VPNs do nothing in
  this space.

- Tor Browser prevents tracking across first party domains with the
  aforementioned intelligent isolation. VPNs do nothing in this space.

- Tor Browser does better at preventing HSTS or alt-svc tracking. VPNs do
  nothing in this space.

Read more: [Tor Browser design document][tb-design]

# Torrenting copyrighted media

First: I'm not saying I support this activity. But many people do it, so if
you're going to ...

[Don't torrent over Tor][torrent-over-tor]. **USE A VPN**.

Tor is an important resource that [many people depend on][tor-users] in order
to have free access to the Internet. **This resource is limited**. When you
selfishly torrent the latest episode of the Big Bang Theory over Tor, you take
away valuable bandwidth that other people actually need.

Further, there are under [1000 Tor exits][relay-flags] operated by an even
smaller number of volunteers all over the world. When you torrent over Tor in
order to avoid legal trouble, **you put that legal trouble on those exit
operators (like me) instead**. That makes you an asshole.

When you use a VPN, you pay a company. You **pay** to have a piece of their
**paid for** bandwidth capacity to do whatever you want with. Some VPN
providers are **sizeable businesses** and have decided **they are well equipped
to deal with legal issues from their customers' traffic**.

# Anonymizing non-web browsing traffic

If latency is really important to your application, using Tor is probably a
mistake. Tor is getting better every year and there's exciting
research/development opportunities ahead that I hope to be a part of that will
help in the latency/throughput department, but Tor can still be too high
latency for applications such as video games.

If the applicaiton uses UDP (and isn't a limited subset of DNS), Tor doesn't
support it.

SSH works reasonably over Tor, but does have some noticable additonal latency.
SSHing into a box running a non-anonymous single-onion service should be faster
than SSHing into one through an exit node or a regular onion service. Email
works great over Tor. IRC does too. Many people claim to have success watching
videos (e.g. from YouTube) over Tor, and those that claim it won't work
generally seem to be parroting "common knowledge" and don't actually know.
Mumble (VOIP) works pretty well over Tor.

If you must use or choose to use a VPN instead of Tor to anonymize your
traffic, note how limited the anonymity gains are by rereading other sections
and applying their content to this context. These limited gains may fit your
adversary model just fine.

# Avoiding geo-blocks

If the service doing the geo-blocking hasn't already determined that the VPN
you are using is helping people circumvent geo-blocks and blocked them, then
this is a great reason to use a VPN. Tor (Browser) might work too. A common
reason to use a VPN is to avoid geo-blocks for video streaming sites
specifically; while Tor's performance is getting better every year, a VPN is
probably a better choice right now.


# VPN vs your ISP

Yes VPNs hide everything about what you're doing on the Internet from your ISP.
So does Tor (Browser). Only sophisticated attacks (e.g. website fingerprinting)
allow them to determine what you're doing, and these apply to VPNs, Tor, and
every other "thing" like them that actually exists off paper. Tor has taken some
measures to mitigate attacks such as website fingerprinting, but I am not convinced
they are effective at this time.

# VPN vs a government

This is a tough one, but if you believe your government is watching your
traffic between you and your ISP or can otherwise compel  your ISP to tell it
information about your activities, I think it is foolish to believe they cannot
do the same with your chosen VPN provider. If you really believe your VPN
provider wouldn't cooperate, then I bet the datacenter in which their servers
reside or the upstream autonomous systems would do so, if they aren't already.
This type of adversary is extremely powerful and not even Tor can totally
protect you. Search terms in this space include "traffic correlation." In the
name of brevity I'll stop here after saying one last thing: it doesn't matter
how many hops or how much technology you have in the middle of your connection
if your adversary can watch traffic sufficiently close to you and to your
ultimate destination, and you should not limit yourself to an adversary model
that requires them to *run* the hops as opposed to simply watch Internet
traffic near them.

# Additional stuff

I might add more sections to this post in the near future, but for now I need
to stop. So here is some additional reading you might find interesting.

## Reading

- [[Adding a VPN to Tor probably isn't gaining you anything|vpn-tor-not-mRikAa4h]]

- [[General Tor Browser security (anti-)tips|about-to-use-SkxEFK1m]] including why you
  shouldn't read too much into fingerprint test site results when using Tor
Browser and especially when you don't now what the results mean; the
value of adding extra extensions to Tor Browser; and why it's fine to log in to
"real" accounts in Tor Browser.

- [Millions of regular people use Tor for regular reasons all over the world][tor-users]

- You can use Tor Browser without accessing """the deep web.""" When defined as
  Tor onion services, """the deep web""" [is tiny and basically no one uses
it][deepweb-size].  You're no more likely to get malware from a site ending in
.onion than you are from a .com site. (What does """deep web""" [even mean][what-deepweb]?)

- [[I know what I'm talking about|about-me-6eKe2i5v]] and I'm not trying to sell you anything. <sup>I do make mistakes though</sup>

## Thoughts

- Some sites (like banks) are super-mega distrustful of Tor users. This is
  unfortunate.  Until we make a future where so many people are using Tor for
benign, boring things, foregoing Tor and using a VPN to access these sites may
be the best you can do.

------

[[!tag tor tor-browser vpn]]
