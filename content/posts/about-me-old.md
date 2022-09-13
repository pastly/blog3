---
title: "About Me (old)"
date: 2016-08-28
slug: 2016-08-28-about-me"
type: posts
draft: false
categories:
  - default
tags:
  - meta
---

[about-me]: {{< ref "about-me" >}}

*This post first appeared on my old blog in August 2016. It is preserved, but
maybe not updated, here. My latest about me page is [here][about-me].

---

[Rob Jansen]: https://www.robgjansen.com/
[Nick Hopper]: https://www-users.cs.umn.edu/~hoppernj/
[Paul Syverson]: https://www.syverson.org/
[Aaron Johnson]: https://ohmygodel.com/

[2019-hotpets]: https://www.petsymposium.org/2019/hotpets.php
[2019-secdev]: https://secdev.ieee.org/2019/Home/
[2018-tops]: https://dl.acm.org/citation.cfm?id=3287762
[2018-ccs]: https://www.sigsac.org/ccs/CCS2018/
[2018-foci]: https://www.usenix.org/conference/foci18
[relays]: https://metrics.torproject.org/rs.html#search/pastly
[flashflow]: https://flashflow.pastly.xyz

I work for the Naval Research Lab. From 2016-2020 I worked among world experts
on privacy and security performing research and development on Tor, and
sometimes the Internet in general. You will find this reflected in my
publications below.

As of 2021 I still work for NRL but not to work with Tor.
I want to keep doing privacy/security things in my free time, but I'm currently
looking for monetize-able hobbies, and in my experience, privacy/security stuff
isn't easily monetize-able. Contact me if you have an idea, and ideally funding
go with it.

As for running relays: I have managed 10s of relays over the years,
many of which are exits. At times my fleet would push 1 Gbps all day every day
(not *capacity*, but *usage*). Please contact
me if you would like to support the operation of high-quality up-to-date relays
and/or relays running new experimental versions of Tor. I will also run exits
with your support. The relays I run can be found [here][relays] <small>(link likely to
stop working without me noticing)</small>.

# Publications

## Peer-Reviewed Journals and Conferences

<big>**Self-Authenticating Traditional Domain Names**</big>
[[pdf](/papers/secdev19-satdomains.pdf)]
[[code](https://github.com/pastly/satis-selfauth-domains)]  
[IEEE Secure Development Conference (SecDev 2019)][2019-secdev]  
[Paul Syverson][] and Matthew Traudt

<big>**KIST: Kernel-Informed Socket Transport for Tor**</big>
[[pdf](/papers/kist-tops2018.pdf)]
[[acm](https://dl.acm.org/citation.cfm?id=3278121)]  
[ACM Transactions on Privacy and Security (TOPS 2018)][2018-tops]  
[Rob Jansen][], Matthew Traudt, John Geddes, Chris Wacek, Micah Sherr, and [Paul Syverson][]

<big>**Privacy-preserving Dynamic Learning of Tor Network Traffic**</big>
[[pdf](/papers/tmodel-ccs2018.pdf)]
[[data](https://tmodel-ccs2018.github.io/)]  
[25th ACM Conference on Computer and Communication Security (CCS 2018)][2018-ccs]  
[Rob Jansen][], Matthew Traudt, and [Nick Hopper][]

## Peer-Reviewed Workshops

<big>**Does Pushing Security on Clients Make Them Safer?**</big>
[[slides](/papers/hotpets19-pushing-security.pptx)]
[[pdf](/papers/hotpets19-pushing-security.pdf)]  
[12th Workshop on Hot Topics in Privacy Enhancing Technologies (HotPETs 2019)][2019-hotpets]  
Matthew Traudt and [Paul Syverson][]

<big>**HSTS Supports Targeted Surveillance**</big>
[[pdf](/papers/foci18-paper-syverson.pdf)]
[[foci](https://www.usenix.org/system/files/conference/foci18/foci18-paper-syverson.pdf)]  
[8th USENIX Workshop on Free and Open Communications on the Internet (FOCI 2018)][2018-foci]  
[Paul Syverson][] and Matthew Traudt

<!-- ## Peer-Reviewed Posters and Abstracts -->

## Tor Proposals

[ff-torspec]: https://gitweb.torproject.org/torspec.git/tree/proposals/316-flashflow.txt
[ff-email]: https://lists.torproject.org/pipermail/tor-dev/2020-April/014243.html

<big>**FlashFlow: A Secure Speed Test for Tor (Parent Proposal)**</big> [prop#316][ff-torspec], 2020  
Matthew Traudt, [Rob Jansen][], [Aaron Johnson][], and Mike Perry  
[Discussion][ff-email]

## Other

<big>**FlashFlow: A Secure Speed Test for Tor**</big>
[[arxiv](https://arxiv.org/pdf/2004.09583.pdf)]  
Technical Report arXiv:2004.09583 [cs.CR] (arXiv 2020)  
Matthew Traudt, [Rob Jansen][], and [Aaron Johnson][]

<big>**Tor’s Been KIST: A Case Study of Transitioning Tor Research to Practice**</big>
[[pdf](/papers/kistdeploy-arxiv2017.pdf)]
[[arxiv](https://arxiv.org/pdf/1709.01044.pdf)]  
Technical Report arXiv:1709.01044 [cs.CR] (arXiv 2017)  
[Rob Jansen][] and Matthew Traudt

# Contact

Personal: **sirmatt |at| ksu d0t edu**  
Tor: **pastly |at| torproject d0t org**  
Work: **matthew d0t traudt |at| nrl d0t navy d0t mil**  
[GPG 0x83BCA95294FBBB0A](/pastly.pubkey.txt)  
Reddit: /u/system33- and /u/pastlytor. Any other username claiming to be me is lying.  
IRC: pastly on irc.oftc.net  

# Projects

In general, you can find code I write in public on
[GitHub](https://github.com/pastly) and
[Tor's GitLab](https://gitlab.torproject.org/pastly).

## Simple Bandwidth Scanner

[Project link](https://github.com/torproject/sbws)

Some of the Tor directory authorities run bandwidth scanners to measure the
bandwidth of relays and include their measurements in their network status
votes. Clients use the consensus of these weights to inform their path
selection process with the hope that every circuit they build will have roughly
equal performance, regardless of the relays chosen. This achieves a form of
load balancing.

Historically, the directory authorities that ran bandwidth scanners (bandwidth
authorities), ran [torflow](https://gitweb.torproject.org/torflow.git/).
Time passed, it slowly become less maintained, and
the collective knowledge of how it worked slipped away.

Simple Bandwidth Scanner (sbws) aims to be a quick to implement, easy to
maintain replacement for torflow.

## KIST

KIST is a new scheduler for Tor. It is merged into Tor code as of 0.3.2.9. It
prioritizes low-bandwidth, bursty traffic (web traffic) over high-bandwidth,
continuous traffic. See my relevant publications for more information.

## BM - Blog Maker

[Project link](https://github.com/pastly/bm)

BM is barely maintained.

<!-- This blog-like website is created with bm. -->

BM is a set of scripts that use common GNU utilities to dynamically create a
static blog. See the README at the project page linked above for more
information.

<!--
## Ricochet

[Project link](https://github.com/pastly/ricochet/tree/group-messaging)

For my senior project, I worked on adding group chat to Ricochet. With the help
of my advisor, [Dr. Eugene Vasserman](https://people.cs.ksu.edu/~eyv), I
developed a set of protocols called Shrapnel that can be used for robust,
secure group messaging. 

The progress I made in implementing Shrapnel in Ricochet can be found
[here](https://github.com/pastly/ricochet/tree/group-messaging). I implemented
everything but

* handling chat history inconsistency
* handling group membership inconsistency
* everything GUI

## Movenseed

[Project link](https://github.com/pastly/movenseed)

Movenseed is a python3 script that's handy for continuing to seed files after
moving, renaming, and reorganizing them.

First you run the prework stage either on a directory containing the
correctly-organized files for seeding *or* a `.torrent` file. Then you stop
seeding while you do all the moving and reorganizing you want. Finally, you
run the postwork stage on the directories that have the renamed/reorganized
files in order to create symbolic links to them in the original directory. See
the README at the project page linked above for more information.

Generally speaking, this script is helpful in many instances of semi-manual
data deduplication.
-->

