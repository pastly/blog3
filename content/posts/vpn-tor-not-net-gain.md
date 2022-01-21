---
title: "VPN + Tor: Not Necessarily a Net Gain"
date: 2016-11-12
slug: 2016-11-12-vpn-tor-not-net-gain
type: posts
draft: false
categories:
  - default
tags:
  - tor
  - vpn
---

*This post first appeared on my old blog in November 2016. It is preserved,
but maybe not updated, here.*

---

So many people share the advice to use a VPN in conjunction with Tor, usually by
way of placing the VPN between the user and her guard node (connecting to Tor
through a VPN). More rarely, the advice is given to place the VPN between her
exit and her destination (connecting to a VPN through Tor). On the surface,
these ideas sound good, or at least not bad. The first one especially sounds
like it must help. More encryption is always better, right?

This post will discuss my reasoning for why using a VPN with Tor is not the
obvious security gain that people make it out to be. Users may not lose any safety
by adding a VPN, but they probably aren't gaining any.

[[!toc levels=2]]

----

**Update June 2019**:

- Remember that you have to trust the VPN company to keep themselves secure.
  Why should you add more points of failure?
[This VPN company](https://nordvpn.com/blog/torguard-lawsuit/) made some dumb
mistakes, and tried to sue when it was responsibly disclosed to them
([archive](https://archive.fo/Cvo6n)). I would consider VPN companies much
juicer targets for hackers who want to uncover lots of people doing
illegal/embarrassing things as compared to some random residential ISP.

- Some wording

**Update April 2019**:

- [An anti-VPN security.stackexchange.com
post that I like](https://security.stackexchange.com/a/125008). It argues
the benefits of adding a VPN to Tor is "tenuous at best."

- Rephrase sentence in trust section.

**Update December 2018**: Added some better reasons to not use a VPN through
Tor that should've been added a long time ago.

**Update April 2018**: Here are some additional things I think everyone should
read or be aware of.

- [Opinions from a person I
  respect](https://github.com/epidemics-scepticism/writing/blob/master/misconception.md).
([archive](https://archive.fo/CV4Ji))

- [VPNs lie about their
  geolocation](https://blog.benjojo.co.uk/post/north-korea-dprk-bgp-geoip-fruad),
and it's easy to do ([archive](https://archive.fo/xyABA)).
**See also [*How to Catch when Proxies
Lie*](https://people.cs.umass.edu/~phillipa/papers/imc18-final122.pdf) which
appeared at IMC 2018.**

- [Avoiding relays in certain countries is not
  effective](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-li.pdf)
(PDF) at preventing your traffic from going through those countries.
Furthermore, if you think some countries are *really* part of your *realistic*
adversary model, you should probably consider them network-level adversaries
**that aren't limited to running Tor relays** to begin with.

- [Random gist.github.com
  paste](https://gist.github.com/joepie91/5a9909939e6ce7d09e29), but I don't
agree that you should set up your own VPN box. That's essentially a perfect
fingerprint identifying you to your guard and network-level adversaries along
the way. ([archive](https://archive.fo/YZ6k6))

- [VPN providers do bad lazy things in order to attract more
  customers](https://gist.github.com/kennwhite/1f3bc4d889b02b35d8aa), so they
probably shouldn't be trusted to get any of the hard technical details correct.
([archive](https://archive.fo/HKfiy))

I've added a section about hiding your IP from browser malware. I've also added
some more thoughts/information inline to the body of this post with no
indication about what is new. I've fixed some spelling mistakes.

----


# Trust

First I want to bring up trust. __A VPN is fully, 100%, a single point/entity
that you must trust.__ With Tor, you do not have to trust any single entity or
any single point.
Users don't have to trust every Tor relay that they use in order to stay safe
with Tor. As long as the right ones aren't compromised, working together, or
otherwise malicious, the user stays protected.

VPN users fully trust their VPN. They trust their VPN provider

- to not keep payment information
- to not keep logs
- to not share information with their adversary
- to be competent at keeping their network and machines secure

Should VPN-provider-X be completely trusted? Maybe. Are they completely trusted
by their users? Yes, whether the users realize the amount of trust they are
placing in the provider or not.

Assume for just a moment that using only Tor gives Alice the same about of
"protection" as using only a VPN. Using only Tor, she doesn't have to trust
any single entity. Using a VPN, she has to completely trust her VPN provider.

So why use a tool that _requires_ the user's trust, when she can use a
tool that doesn't?

This brings up the question: __If Alice chooses she 100% trusts her VPN provider
and wants to use Tor with a VPN, does the VPN add any value?__ I will address
this question in two parts based on whether the VPN comes "before" or "after"
Tor.

# Connect to Tor through a VPN

Now I'll start with what is easiest to actually accomplish and is recommended
most often. I prefer to discuss this as a series of reasons why someone would
even think about using a VPN in this way.

## Tor is Blocked

For whatever reason, Tor is blocked for Alice. Maybe her company has a really
strict firewall or her country has a super strict firewall. But apparently the
firewall wouldn't block a VPN.

Alice should try using a Tor bridge first. A bridge is simply an unlisted Tor
guard relay. If she was getting blocked because she was trying to connect to an
IP known to be a Tor relay, this would help.

If that doesn't work, maybe her traffic is being blocked because it looks like
Tor traffic. It _is_ fingerprintable after all. If this seems to be the case,
then Alice should try using a bridge with a pluggable transport. Pluggable
transports make Tor traffic look different so it can (hopefully) not be
fingerprinted and then blocked. obfs4 is a popular PT that makes the Tor traffic
between Alice and her bridge look like encrypted garbage. meek is another PT
that makes it look like Alice is talking to a website in the Amazon or Microsoft
cloud.

## Hide Tor Usage from ISP

First, Alice should consider whether or not her adversary is even capable of
extracting information from her ISP. Is what she's doing even illegal where she
lives? Is it embarrassing? To what lengths will her adversary go (or can her
adversary go) in order to figure out who she is? If Alice is just trying to hide
an embarrassing habit from her spouse or circumvent her incompetent country's
censorship, hiding her Tor usage may not even be necessary.

Furthermore, if Alice isn't really up to anything bad, by *not* hiding her Tor
usage, she helps reduce Tor's bad stigma. [Many people use Tor for a wide
variety of reasons](https://www.torproject.org/about/torusers.html.en). And if
Alice believes Tor usage is enough to get her on a list of potentially bad
people, she should be proud of that fact. She's not bad, and she's lowering the
quality of that list. If everyone used Tor, everyone would be on the list, and
the list would be worthless.

If Alice determines that she really does need to hide her Tor usage, she should
first consider using bridges or bridges with pluggable transports. See the
preceding section for information on those.

## Hide True IP from Global Passive Adversary

I would like to preface this with: a global passive adversary (GPA) isn't
something everyone should just assume they have to deal with.

A GPA can watch and record Internet traffic "all over," where "all over" is a
large enough number of places that, in the context of Tor, they can
watch/record traffic entering the Tor network as well as watch/record traffic
leaving the Tor network. One way to accomplish this would be for the GPA to run
Tor relays themselves, but that isn't a necessity. They could work
with/hack/compromise ISPs and ASes "all over" until they get a good view of
Tor's edge traffic.

A VPN between Alice and her entry point into the Tor network sounds like it
would help, right? The GPA watching and correlating traffic will correlate her
traffic to her VPN's IP address, not hers.

My rebuttal is best summed up with rhetorical questions: if her adversary is
powerful enough to be able to watch traffic entering and exiting the Tor
network, aren't they also capable of watching traffic enter and exit a single
VPN provider?

Since VPNs are so popular, isn't it likely that the GPA has already done
something to compromise the most popular ones?

Why would anyone ever assume that the GPA they're protecting themselves against
would be stopped dead in its tracks by a VPN? If they can watch traffic leaving
"enough" of the almost 1000 Tor exits and "enough" of the roughly 2500 Tor
guards, then why would all of the following be impossible?

- extracting information from the VPN provider via the legal system
- extracting information from ISPs/ASes on both sides of the VPN provider
- gaining permission to watch traffic on the VPN's network
- watching traffic on the VPN's network (via compromise)

If Alice thinks she has a GPA to worry about, I think she is a fool for
assuming the GPA can't find her behind a VPN.

## Hide True IP from Browser-based Malware

Historically these exploits have seemed very valuable. They've only ever been
found deployed in the wild against people doing terrible things. They've only
targeted Windows users (likely because that was the largest demographic and the
one that required the least amount of work for the most amount of reward). If
you're not doing terrible things, you're probably not going to run into one of
these exploits. If you're not using Windows, they're probably not going to work
on you. Either by not being a shitty person or by not using the most popular
operating system you avoid these exploits.

But maybe you don't agree that these exploits are rare and targeted. Okay ...

If you're assuming your adversary can break Tor Browser enough to make a web
request that doesn't go over Tor (or otherwise collect identifying information
about you or your computer), they're probably capable of a lot more.

If you think they can break out of Tor Browser entirely and run arbitrary
commands as your non-root user, then something like Tails is probably more
effective against this adversary than a VPN.

If you think they can both break out of Tor Browser and gain root privileges on
your computer, then you're screwed and Tails won't help, a VPN won't help, and
Whonix probably won't help either. Get off the Internet.

# Connect to a VPN through Tor

I will now switch gears to discussing connecting to a VPN through the Tor
network. People usually consider doing this because they want to appear to have
an IP address that doesn't change and isn't associated with Tor. Doing this
throws away the vast majority of the security gains that Tor gets you. It ruins
Tor so much, and you have to trust the VPN company so much, that you might as
well not even use Tor at all.

## Traffic Pattern

When you use Tor Browser normally, it does lots lots of intelligent stuff to
keep you safe. [Tor Browser is a lot more than Firefox with some preconfigured
security settings and some addons][TB design].

[TB design]: https://www.torproject.org/projects/torbrowser/design/

If in some tabs you are visiting Facebook (perhaps even with your real daily
account) and in some other tabs you on Wikipedia researching an accurate
history of your abusive government, the traffic and the local state from the
Facebook tabs will not touch the traffic or state from the Wikipedia tabs. The
traffic from Facebook tabs *regardless of destination domain* will not use the
same circuits (paths) through the Tor network as traffic from Wikipedia tabs,
not even if they use the same ad network or content delivery network.  You can
never recreate this behavior in any other browser without modifying its source
code and recompiling it. This is beyond simple configuration options.

If you connect to a VPN over Tor, this traffic separation goes away completely.
You build a *single* circuit through the Tor network, and over this circuit you
connect to your VPN. All your Facebook and Wikipedia traffic travels the same
path right next to each other. If you tunnel other things over this VPN
connection, those things are right there too. All the SSH traffic, IRC traffic,
IMAP, SMTP, or OS update traffic that you generate through this tunnel is right
next to each other. Worse, depending on how you managed to get this
VPN-over-Tor setup working, you may have even broken the local state separation
of Tor Browser. If any of this traffic is identifying of you, you've
potentially tainted all of your traffic.

## Speed

I should preface this with: I've never actually tried this, but have a good
enough understanding about how this stuff works that I'm confident I can make
some claims.

The most common way to connect to a VPN, as far as I'm aware, is with OpenVPN.
OpenVPN works best when using UDP, but it technically supports using TCP. Tor
cannot transport UDP, so if using OpenVPN, then the user must us it in TCP mode.

What's so bad about TCP mode? The details get rather technical unfortunately,
but I'll try to sum it up.

TCP guarantees reliable in-order delivery of data. Among other things, it
accomplishes this by retrasmitting lost packets.

When using Tor, Alice has a TCP stream between her exit and her destination. If
her destination (from the point of view of the exit) is an OpenVPN server using
TCP, then there is a TCP stream within a TCP stream. If what Alice is ultimately
doing uses TCP (like browsing the web, for example), then the Tor TCP stream
contains an OpenVPN TCP stream that contains Alice's actual TCP stream. If any
of these streams detect packet loss, all of them will notice, back off on their
transmission rates, and retransmit the packets they think got lost. This is
absolutely terrible for performance.

Tor isn't really that slow these days ... unless you do something crazy like
this.

## Security

So if Alice decides she doesn't care about the huge performance hit, what does
she get? She certainly gets the non-Tor IP address she wanted. Does she gain
anything that I discussed in the previous section about [connecting to Tor
through a VPN](#connect-to-tor-through-a-vpn)?

Alice's ISP will see her talking to a Tor guard. She could use a bridge (or even
a bridge with a pluggable transport) to prevent this. Again see [this
section](#connect-to-tor-through-a-vpn) for information on bridges.

Will she hide her true IP address from a global passive adversary? I already
explained why thinking an adversary _can't_ get information out of a VPN provider
but _can_ perform traffic analysis attacks on Tor users is silly. So no, if
she's trying to protect herself from a GPA, she shouldn't consider using Tor to
connect to a VPN any safer than just using Tor in my opinion.

Finally, there's the matter of [trust](#trust) to consider again. Alice must be
sure her VPN provider is worthy of the trust she will be placing in it. She must
have paid her VPN provider in a way that can't be traced back to her. She must
be sure that the VPN provider doesn't keep traffic or connection logs. She has
to trust _herself_ to never mess up and connect to her VPN without Tor. And for
this VPN to be of any benefit at all, she must convince herself that her
adversary can't somehow work with the VPN provider, compromise the VPN provider,
or work with/compromise ISPs and ASes near the VPN provider.

# Final Thoughts

I'm usually one of the first to remind people that everyone's security needs are
different. I generally hate it when people immediately jump to assuming that the
user asking for advice needs protection from a super powerful adversary. Not
everything I've said may apply to you, the reader. And maybe in my limited
experience I've missed something that you have a question about. I've seen many
discussions about using a VPN with Tor though, and I hope very long-winded post
will help you made an informed decision.

---
sources: [number of Tor exits and
guards](https://metrics.torproject.org/relayflags.html?start=2016-08-14&end=2016-11-12&flag=Exit&flag=Guard)
