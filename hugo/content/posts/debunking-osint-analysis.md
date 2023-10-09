---
title: "Debunking 'OSINT Analysis of the TOR Foundation' and a few words about Tor's directory authorities"
date: 2021-02-12
slug: 2021-02-12-debunking-osint-analysis
type: post
draft: false
toc: true
categories:
  - default
tags:
  - tor
  - not-me
---

The following post **was not written by me.** It was written by [Julien Voisin](https://dustri.org/) and
[posted on his blog](https://dustri.org/b/debunking-osint-analysis-of-the-tor-foundation-and-a-few-words-about-tors-directory-authorities.html) in October 2018.
I am sharing it here, unedited except as noted below, according to the [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license of the post.

Edits made:

- Add table of contents.
- Change local links to point to my copies of the paper and its figures, not Julien Voisin's copies.

The paper it talks about is old news at this point (from 2018), but I see someone stumble upon it every few months ... instances that are *just* spread out enough
I can never remember where this amazing post is on the web. Now I can't lose it.

-----

Title: Debunking "OSINT Analysis of the TOR Foundation" and a few words about Tor's directory authorities  
Date: 2018-10-04 15:00

I have spent years on [Tails](https://tails.boum.org)' IRC channel answering
questions from various users, amassing a pile of personal notes about the internals
of both Tor and Tails in the process.

A friend of mine linked me an ["interesting" paper](https://arxiv.org/abs/1803.05201)
([local mirror](/debunk-osint/paper.pdf))
entitled `OSINT Analysis of the TOR Foundation`, and was wondering how much
trust to put in it. I read it, and decided that it was so hilariously bad that
it deserved a blogpost. It's also a nice opportunity to explain a few things
about the [directory authorities](https://www.torproject.org/docs/faq#KeyManagement) (dirauth). 

The post is in two parts: first, a rough explanation about what the dirauth
are and how resilient is the tor network with regard to them,
then a complete review of the paper.

# Tor and the dirauth

The Tor network is mainly composed of relays run by volunteers, with various
attributes:
[exit](https://metrics.torproject.org/rs.html#search/flag:exit),
[fast](https://metrics.torproject.org/rs.html#search/flag:fast),
[guard](https://metrics.torproject.org/rs.html#search/flag:guard),
[hsdir](https://metrics.torproject.org/rs.html#search/flag:hsdir),
[running](https://metrics.torproject.org/rs.html#search/flag:running),
[stable](https://metrics.torproject.org/rs.html#search/flag:stable),
[valid](https://metrics.torproject.org/rs.html#search/flag:valid),
[badexit](https://metrics.torproject.org/rs.html#search/flag:badexit),
[v2dir](https://metrics.torproject.org/rs.html#search/flag:v2dir),
 … but also [authority](https://metrics.torproject.org/rs.html#search/flag:authority).

[Tor 0.0.2](https://gitweb.torproject.org/tor.git/tree/ChangeLog?h=tor-0.0.2&id=161d7d19aeead874831c40c4824551204c6afe21),
released in 2004, introduced *Directory Authorities*, servers that served
(duh.) cryptographically signed directory documents, containing a list of all
relays along with their associated metadata (capacity, version, uptime, …) and
status.

But the first version of the directory protocol didn't prevent a lying
authority from providing a distorted view to some clients. This is why the
second iteration implement cryptographic signature, to allow the client to only
trust the directory documents signed by strictly more than half of all the
dirauth.

The third version (which happens to be the current one) provides support for
offline storing of critical cryptographic material for the dirauth, so that
keys don't have to be stored in plain-text on the machines anymore.
Furthermore, it introduced a nicely constructed consensus for the dirauth,
instead of asking the client to aggregate all the separate data, to fight
partitioning attacks.

It's possible to take a look at what the consensus looks like [here](https://consensus-health.torproject.org/).

## How are new relays registered?

When a new relay comes online, it uploads its relay descriptor to a dirauth, to
register itself with the tor network. Each dirauth is taking its view of the
network and every hour gossip their 'vote' of the view of the network (which is
essentially all the relay descriptors that they are aware of, and the bwauth
measurement results) with the other directory authorities, and that is all
merged into one 'consensus document' that is the global view of the network for
a certain duration. That consensus document is fed to the fall-back
authorities, who are the frontlines to clients coming online and needing to
load the current state of the network.


## Who controls the dirauth?

There are currently [10 relays with this flag](https://metrics.torproject.org/rs.html#search/flag:authority):

- `bastet`, in the USA, run by [Stefani Banerian](https://we.riseup.net/stefani), hosted by [riseup](https://riseup.net)
- `dannenberg`, in Germany, run by [Andreas Lehner](https://media.ccc.de/search?q=Andreas+Lehner), hosted by the [CCC](https://www.ccc.de/)
- `dizum`, in the Netherlands, run by Alex de Joode from [sabotage.org](https://www.google.com/search?q=site:sabotage.org+-handbook), hosted by [XS4ALL AS](https://www.xs4all.nl/)
- `faravahar`, in the USA, run by [Sina Rabbani](https://twitter.com/wwwiretap ), hosted on [Rethem Hosting](http://www.rethemhosting.net/) infrastructure.
- `gabelmoo`, in Germany, hosted by [Sebastian Hahn](http://sebastianhahn.net/) (you might have [heard about him]( https://www.welt.de/politik/deutschland/article129734293/Die-NSA-spaehte-einen-Erlanger-Studenten-aus.html)) in an [university]( https://en.wikipedia.org/wiki/Deutsches_Forschungsnetz )
- `longclaw`, in Canada run by the *birds* from [riseup]( https://riseup.net ), hosted on [Koumbit](https://www.koumbit.org/)
- `maatuska`, in Sweden, run by [Linus Nordberg]( https://nordberg.se ), hosted by the [DFRI](https://en.wikipedia.org/wiki/DFRI)
- `moria1`, in the USA run by [Roger "arma" Dingledine](https://en.wikipedia.org/wiki/Roger_Dingledine) at the MIT's AS: `AS3`
- `tor26`, in Austria run by [Peter Palfrader]( https://www.palfrader.org/ ) on Tele2 Telecommunication GmbH's AS: `AS8437`

Additionally, there is a bridge authority, that isn't a v3 directory one,
listed here only for completeness' sake:

- <s>`bifröst`, in the Netherlands by [isis agora lovecruft](https://www.patternsinthevoid.net/) on [Greenhost](https://greenhost.net/)'s AS</s>
- `Serge`, in the USA, run by [George "gman999" Rosamond](https://github.com/gman999) from [torbsd.org](https://torbsd.org/), hosted on [NYI](https://www.nyi.net/).


All of them are either in North-america or in Europe. I'm not in the business
of [doxing]( https://en.wikipedia.org/wiki/Doxing ) people, but it's pretty
easy to find the social graph and nationality of all the admin in the
list, their relationship to the Tor project, and even to have a beer with some of them :)

## What happens to the network if the dirauth goes down?

If the authorities were all shut down, clients would still be able to download
the list of relays: your client doesn't actually get the relay documents
directly from the authorities, but from caches from Tor nodes with the
[V2dir flag](https://metrics.torproject.org/rs.html#search/flag:v2dir).
Your tor client has as well a local cache anyway.

As for compromised directory authorities, starting from the version 2 of the
directory protocol, on top of downloading the actual relay documents, your
client is also getting hashes of the relay documents signed by other
authorities: relay documents will only be trusted if they are signed by
at least half of the authorities. If one or two or three authorities were to be
compromised, they won't be force clients to accept a distorted versions of the
consensus.

## Can't we replace the authorities with something more distributed?

It's a [non-trivial](https://www.freehaven.net/anonbib/#wpes09-dht-attack)
problem.

## Attacks on the dirauth

I discussed a bit with [nextgens](http://florent.daigniere.com/) and *others* about the dirauth,
and it's actually not that trivial to influence them.  The goto way would be to
simply pop them, but I do trust their respective maintainer to have deployed a
bunch of fancy mitigations and monitoring.

An other way would be to influence them, by taking control of the
*pipes* of the majority of the dirauth to influence their measurements.
Fortunately, the dirauth aren't really doing measurements on their own:
[bandwidth authorities](https://gitweb.torproject.org/torflow.git/tree/README)
(bwauth) are, and those are transmitting their calculations to the dirauth they
have a pre-established relationship with.  Some bandwidth authorities are being
run by dirauths, but most of them are not being run on the dirauth machine
itself, but are 'hidden' elsewhere on the network

# The paper

## Author and context

The paper was written by Maxence Delong, Eric Filiol, Clément Coddet, Olivier Fatou and Clément Suhard,
from the [ESIEA](https://www.esiea.fr/), in Laval,
more specifically, from the Operational Cryptology and Virology Laboratory (C + V)<sup>O</sup>.
At this time, everyone but Eric Filiol [was a student](https://www.esiea.fr/techday-2017-zoom-sur-le-campus-de-laval/)

[Eric Filiol](https://sites.google.com/site/ericfiliol/) is
known for pretending to have broken AES in 2002 (he [didn't](https://eprint.iacr.org/2002/149)),
and in 2003 (he still [didn't]( https://eprint.iacr.org/2003/022.pdf )) and Tor
in 2011
(he [didn't either]( https://blog.torproject.org/rumors-tors-compromise-are-greatly-exaggerated)),
and for being the *architect and designer* of [DAVFI]( http://www.davfi.fr/index_en.html ),
a French "new generation anti-malware solution",
known for a being a phenomenal (and extraordinary expensive)
[source of fun]( https://news0ft.blogspot.com/2016/06/le-gachis.html ).

The paper was presented at the
[13<sup>th</sup> International Conference on Cyber Warfare and Security (ICCWS 2018)]( http://www.ndu.edu/ICCWS-2018/ ),
and apparently underwent a "double-blind peer review process". The conference
is organised by [Academic Conferences and Publishing International Limited](https://www.academic-conferences.org/conferences/iccws/),
organizers of a [bunch of conferences](https://www.academic-conferences.org/conferences/).

The [blog](https://cvo-lab.blogspot.com/) of the Operational Cryptology and Virology Laboratory (C + V)<sup>O</sup>
published a [blogpost]( https://cvo-lab.blogspot.com/2018/03/osint-on-tor-foundation-update.html )
entitled "OSINT on the TOR Foundation (Update)", by Eric Filiol,
containing two exaggerations (amongst, as usual, various typos):

> As we shown on our paper “OSINT Analysis of the TORFoundation”, we worked on
the funds and proved that the US government is deeply involve with
arpproximatly 85% of the funds in 2015. 

The paper states the following:

> As we can see, at least 58.20%
of the total funds are coming from different departments of
the US government. The status of RFA (Radio Free Asia)
Contract is unclear and there are persistent allegations and
testimonies (Prados, 2017; Levine, 2015) or even suggestions
that it could be strongly connected to the CIA more than
expected (Levine, 2015). Would this suspicion be true, the
rate of funds from US government-related entities would
grow up to 85.24%.

There is a difference between a *suspicion*, and the blogpost's *affirmation*,
especially when it changes a number from *58.20%* to *85.24%*.

> Secondly, we had some reasons to believe that the US government has strong
links with The TOR Project Inc. via Roger Dingledine who made an internship in
NSA and with some presentations in front of high authorities like the White
House and the FBI. 

I don't think that doing an Summer internship at the NSA qualifies as a "strong
link". About the presentations, it's well known that R. Dingledine does
a lot of them to law enforcement entities, to improve their view on the
network, and more broadly the Tor ecosystem. A lot [of](https://gnunet.org/tor2013)
[his](https://citp.princeton.edu/event/dingledine/)
[bio](https://cns.ucsd.edu/events/event/tor-anonymous-communications-for-the-dept-of-defense-and-you/)
[for](https://www.nsf.gov/cise/cns/watch/talks/dingledine.jsp)
[various](https://events.ccc.de/congress/2006/Fahrplan/speakers/199.en.html)
[conferences](https://crypto.stanford.edu/seclab/sem-10-11/dingledine.html) are ending with this:

> In addition to all the hats he wears for Tor,
Roger organizes academic conferences on anonymity, speaks at a wide variety of
industry and hacker conferences, and also does tutorials on anonymity for
national and foreign law enforcement.

I don't think that this could be viewed as a credible connection to the US
government.


## Form and sources

It's worth noting that while all the figures used in the paper are unreadable,
it's possible to extract them with `pdfimages` (or to check the [sources](https://arxiv.org/format/1803.05201))
to see that they are in pretty high-resolution, and actually readable:
[Figure 1.](/debunk-osint/fig1.jpg),
[Figure 2.](/debunk-osint/fig2.png),
[Figure 3.](/debunk-osint/fig3.png) and 
[Figure 4.](/debunk-osint/fig4.png).

The *figure 3.* doesn't come with any legend with regard to the used
currency, but since its point is to show a ratio, it doesn't matter much.

Despite a second revision to improve the English and remove the typos, the
paper is still full of typos, *frenchisms*, and oddly worded sentences.
Amusingly, this is the diff between the second and the third (and final at this
time) revision of the paper:

```diff
-\author{Maxence Delong$^{1}$, Eric Filiol$^{2}$, Clément Coddet$^{3}$, Olivier Fatou$^{4}$, Clément Suhard$^{5}$}% <-this % stops a space
+\author{Maxence Delong, Eric Filiol\thanks{Contact author: \url{filiol@esiea.fr}}, Clément Coddet, Olivier Fatou, Clément Suhard\\
+        ESIEA Laval, Operational Cryptology and Virology Laboratory $(C + V)^O$ \\ 38 rue des Drs Calmette et Gu\'erin 53000 Laval France}% <-this % stops a space
```

E. Filiol is the only one with an email address, and apparently the main author
of the paper.

About the sources of the papers, almost a third (3/10) of them
are from "Filiol et al."


## Insinuations

The paper is making several baseless/inflated insinuations,
also known as [loaded questions](https://en.wikipedia.org/wiki/Loaded_question),
a classic fallacy technique.

> Officially, this foundation has no
> link with US government (any other one) and is independent (Dingledine, 2017).
> There is a growing feeling that this may not be the case.

<!-- -->

> Recurrent questions arise that put this apparent independency into question: what if
> the US government was behind the TOR network and somehow controls it?

<!-- -->

> In fact, the TOR project is an implementation of a concept born in the US Naval Research
> Laboratory (Goldschlag et al., 1996; Syverson et al., 1997). Paul Syverson is the designer of the routing protocol
> and was part of the original development team of the TOR network. Hence the TOR infancy was clearly linked
> with the US government and still is.

<!-- -->

> Furthermore, Roger Dingledine spent a summer in internship in the NSA, so we
> can suppose that he has kept a few contacts in there

<!-- -->

> The owner is Roger Dingledine, one of the three creators of the TOR
> Project (and a former NSA employee).

Roger only did a Summer internship at the NSA, I wouldn't call him a "former NSA
employee".

## Sloppy research

The title of the paper is "OSINT Analysis of the TOR Foundation", and refers
the "TOR foundation" or "foundation" at least 40 times in the paper,
as well to a *company* and a *firm*, but there are no such things:
[The Tor Project, Inc.]( https://en.wikipedia.org/wiki/The_Tor_Project,_Inc )
is a "Massachusetts-based 501(c)(3) research-education nonprofit organization".
Moreover, the proper capitalization is `Tor` to refer to the project, and `tor` to
refer to the client or the network.

The authors didn't do a proper job to find the *current* Tor specification:

> In this part, we will talk about the directory authorities (see
> https://svn.torproject.org/svn/tor/tags/ tor-0_2_1_4_alpha/doc/spec/dir-spec.txt for details).

The canonical link for it is <https://gitweb.torproject.org/torspec.git/plain/dir-spec.txt>
The linked `Tor 0.2.1.4-alpha` was released in 2008-08-04, **ten years** before the publication
of the paper.

The article doesn't understand the concept of pseudonymity:

> It is a real problem for the network: do users can trust people
> they do not know? Where do these people come from? What
> is their background?

The Tails developers are all pseudonymous, it doesn't prevent the project from
being used and trusted by [thousands of people](https://tails.boum.org/news/report_2018_08/#index10h1)
around the world, and endorsed by [many](https://tails.boum.org/press/index.en.html).

Some famous projects have (or used to have) pseudonymous contributors:
[Bitcoin](https://en.wikipedia.org/wiki/Satoshi_Nakamoto),
[Truecrypt](https://en.wikipedia.org/wiki/TrueCrypt),
[DOTA](https://en.wikipedia.org/wiki/IceFrog), …
most of Wikipedia's contributors are too,
and all of those projects are used and trusted.

I'm way more comfortable knowing that the directory authorities aren't all
managed by Tor employees. Moreover, only a single authority (two when the paper
was written) is managed by well known collectives/pseudonymous people.

All of them are well established entities, known and trusted by many. Saying
that they are unknown and with a mysterious background is a pretty bold
statement. Moreover, "where do these people come from" is a pretty irrelevant
question.

> Peter Palfrader was the owner of tor26
> (the first directory authority which does not belong to Roger
> Dingledine). Released in the version tor-0.0.8.1 in October
> 2004, the directory authority is not working anymore.

This is a plain lie:
[tor26 is working continuously](https://metrics.torproject.org/rs.html#details/847B1F850344D7876491A54892F904934E4EB85D)
since at least 5 years.

> If a few people need to be on the Core
> People page, it will be the founder of the TOR Foundation
> and the people running a directory authority. With this
> disappearance, the customers have less information about the
> people who actually handle the network.

Although [Paul Syverson](http://www.syverson.org/) worked with
Roger Dingledine and Nick Mathewson, he never was part of the Tor Project Inc.
He's still doing research on Tor, anonymity and onion-routing though.

On a side note, using the term "customers" instead of "users" is *interesting*:
Tor has nothing to sell, everyone can use the tor network for free.

> There are at
> least 25 research papers coming from Paul Syverson for the
> TOR network. The last example in date was the 18th of
> September 2017 for the version tor-0.3.2.1 which was imple-
> mented by following a paper wrote by Paul Syverson and his
> team from the US NRL only.

Saying that there are "at least 25" papers without naming a single one of them
is not a correct way to provide sources. Referring to a paper by its date 
of publication isn't either. The paper in question being likely
[Never Been KIST: Tor’s Congestion Management Blossoms with Kernel-Informed
Socket Transport](https://www.robgjansen.com/publications/kist-sec2014.pdf) by
Rob Jansen, John Geddes, Chris Wacek, Micah Sherr and Paul Syverson, followed by
[Tor's Been KIST: A Case Study of Transitioning Tor Research to Practice](https://arxiv.org/abs/1709.01044)
by Rob Jansen and Matthew Traudt.

The first paper wasn't written by "Paul Syverson and his team form the US NRL
only": only Syverson and Jansen are from the U.S. Naval Research Laboratory; 
Geddes is from the University of Minnesota while Wacek and Sherr are from
the Georgetown University.

> Officially, TOR is not
> developed anymore by the US government but a major part
> of changes was designed and developed by Paul Syverson
> through the US NRL and some people have work closely
> for the US government (not only among founders).

This is a bold statement without any kind of proof, but because the Tor Project
has a [lot of code](https://gitweb.torproject.org/) split in different projects,
a simple `git shortlog` on `tor`'s source code shows that this is completely wrong:

```
$ git show | grep '^Date'
Date:   Fri Sep 21 09:54:22 2018 -0400
$ git shortlog -s | sort -nr | head -n 25
 16963	Nick Mathewson
  6245	Roger Dingledine
   715	Peter Palfrader
   678	David Goulet
   546	George Kadianakis
   502	Sebastian Hahn
   492	teor
   417	Andrea Shepard
   362	Karsten Loesing
   322	Mike Perry
   300	Andrew Lewman
   268	teor (Tim Wilson-Brown)
   234	Robert Ransom
   221	rl1987
   150	Alexander Færøy
   145	Isis Lovecruft
   137	cypherpunks
   111	Linus Nordberg
    87	Steven Murdoch
    83	Taylor Yu
    77	Yawning Angel
    73	Cristian Toader
    47	Neel Chauhan
    47	Jacob Appelbaum
    46	Paul Syverson
```

In this list, only Paul Syverson has (public) affiliations with the US government.


> We note that the Core People page is not containing infor-
> mation about a few important people in the TOR Foundation.
> This page is not sufficient to have an idea of who are the
> true leaders of the foundation. We have explained who are the
> leaders of the network (directory authorities) but not those
> of the foundation.

The board of director of the Tor project is
[public](https://www.torproject.org/about/board.html.en),
and apparently, the authors of the paper forgot to check the
[Past Contributors](https://www.torproject.org/about/contributors.html.en),
because it documents the role of every single significant past contributor to
the Tor Project.

> Some contractors were hired, Pearl
> Crescent for example (a developer), and were “hidden” by
> the foundation. The TOR foundation asks indirectly a blind
> trust on the source code (due to the huge amount of line) and
> they give the development to people we do not even know.

Pearl Crescent isn't a developer at all, it's a
[company](https://pearlcrescent.com/about/), referred as *Pearl Crescent LLC.* in
the report. Its activity was thoroughly documented on the
[tor-reports](https://www.mail-archive.com/tor-reports@lists.torproject.org/msg00524.html)
mailing list, and their patches publicly (like any other ones) reviewed.

> We discover a few names that are not on the
> Core People page. Rob Thomas, Meredith Dunn, Andrew
> Lewman, Mike Perry and Andrea Shepard are still unknown.


[Rob Thomas]( https://blog.torproject.org/double-your-donation-rabbi-rob-and-lauren-thomas-announce-matching-challenge-supporttor)
is the founder and CEO of [Team Cymru](http://www.team-cymru.com/aboutus.html).

Meredith Hoban Dunn is an accountant, advisor, and banker. She's the one
that signed the [financial audits reports](https://www.torproject.org/about/findoc/2014-TorProject-combined-Form990_PC_Audit_Results.pdf),
and is designated as the treasurer of The Tor Project, Inc in it.

[Andrew Lewman](http://lewman.com/press.html), as indicated on the
[past contributors](https://www.torproject.org/about/contributors.html.en), is the
former Executive Director. He managed the business operations of The Tor
Project, Inc. Played roles of finance, advocacy, project management, strategy,
press, law enforcement liaison, and domestic violence advocacy.
He was (likely, I don't have much details) fired,
and is now running a [shady company](https://www.darkowl.com/)
that does darknet-related-intelligence-magic-stuff.

A quick glance to the
[Which PGP keys sign which packages](https://www.torproject.org/docs/signing-keys.html.en)
page shows that Mike Perry is/used to be the Tor Browser's lead developer.
The financial report indicates that he's a developer, and a quick glance to
the [commits history of tor](https://gitweb.torproject.org/tor.git/log/) quickly confirms this.
He was my mentor during my 
[Google Summer of Code, in 2011](https://blog.torproject.org/gsoc-2011-metadata-anonymisation-toolkit),
when I wrote the first iteration of [MAT](https://mat.boum.org). I'm not surprised that he doesn't
want to appear on the "Core People" page: he's a very private person.

[Andrea Shepard](http://charon.persephoneslair.org/~andrea/) [was](https://www.torproject.org/about/contributors.html.en) a Tor
developer, as shown by a quick `git shortlog`, and as indicated in the
[2015's financial report](https://www.torproject.org/about/findoc/2015-TorProject-combined-Form990_PC_Audit_Results.pdf).
She was brought to the fore during the [Jacob Appelbaum events](https://www.wired.com/2016/06/tor-developer-jacob-appelbaum-resigns-amid-sex-abuse-claims/).

> The TOR Foundation is regularly claiming that the US
> government is not funding anymore the TOR Project (Din-
> gledine, 2017)

This is a plain lie: the document to source this affirmation is Roger's DEFCON 25's
[presentation](https://media.defcon.org/DEF%20CON%2025/DEF%20CON%2025%20presentations/DEFCON-25-Roger-Dingledine-Next-Generation-Tor-Onion-Services-UPDATED.pdf),
which actually shows that Dingledine actually **debunked** the following
"myths" during [his talk](https://www.youtube.com/watch?v=Di7qAVidy1Y), along
with several other ones listed in the paper:

- “I heard the Navy wrote Tor originally, so how can I trust it?”
- “I heard the NSA runs half the relays.”
- “I heard Tor gets most of its money from the US government.”
- “I heard 80% of Tor is bad people.”

The table 2. is right (notwithstanding the typos),
but since it's mostly copy/pasted data from the
[financial report](https://www.torproject.org/about/findoc/2014-TorProject-combined-Form990_PC_Audit_Results.pdf),
it's not surprising.


> We will not develop most of the technical aspects that
> could suggest or confirm that somehow the TOR network
> has been designed or is managed in such a way that a few
> “facilities” are possible and would enable to take control
> over it. As a consequence, taking the control of a reduced
> number of TOR relays (from 450 to 1400 only) would
> enable to reduce the TOR traffic of at least 50 % and would
> greatly ease correlation attacks (about 35 % of the traffic) or
> eavesdropping (about 10 % of the traffic).

Yet an other loaded question, and references to other papers from Filiol; I
might publish my lecture notes about them at some point in the future too.

> As far as the relay bridges management is concerned, it has
been possible to extract slightly more than 2,500 such bridges
thus compromising the alleged ability to bypass censorship.

This has been [debunked]( https://blog.torproject.org/blog/rumors-tors-compromise-are-greatly-exaggerated)
[several]( https://arstechnica.com/information-technology/2011/10/slicing-the-onion-is-tor-vulnerable-or-not/)
[times]( https://lists.torproject.org/pipermail/tor-talk/2011-October/021730.html).


> During our study, in September 2017, we were contacted
> by a user of a custom TOR library. This library is the “node-
> Tor” written in JavaScript and allows the user to create
> and run a node or connect to the TOR network. Further
> exchanges with this person have shown a lot of inconsistency
> and irregularities.

The person here is actually Aymeric Vitte. I sent him an email, and he felt
that Filiol's paper deserved a public response on
[tor talk](https://lists.torproject.org/pipermail/tor-talk/2018-September/044437.html).
I do recommend its reading ;)

> At first, we talk about the way that his node was added
> to the network. For this custom library, the user asked the
> TOR foundation to add a node with this library and after
> an exchange of a few mails the node was accepted and run.
> The library is very different from the original source code.
> To compare very simply those two codes, we just compared
> the number of code lines. We know that the number of code
> lines does not really reflect the effect of the code but between
> the original source code (several hundreds of thousands code
> lines) and the library (only fifteen hundred code lines), we
> can assure that it is very likely that a number of options or
> securities are missing.

They are comparing the number of lines in a minimal javascript
(a [high-level language](https://en.wikipedia.org/wiki/High-level_programming_language))
implementation of Tor, and the *official* full-blown implementation, written in C
(a [kind of low-level language](https://en.wikipedia.org/wiki/High_level_language#Relative_meaning)):
this comparison metric doesn't make any sense.

Moreover, implying that [Tor-node](https://github.com/Ayms/node-Tor) is only
1500 lines of code is a ludicrous claim, given how much [it does](https://www.peersm.com/).


Anyone can add a node to the network, there is no such thing like "ask the TOR
foundation (sic.)" to add one.

> It is not the designer of this code who is responsible
but rather the TOR foundation for accepting a node on the
network with this kind of library. The first problem is that
no one is warned that this node is special and is not running
the official source code. This node owned by a user is not
controlled by the TOR foundation. So if the user is malicious,
he could modify his node and make every change he wants.
If a government wants to include this kind of node to log the
traffic and gather it, he can do it very simply and without
triggering any alert.

Having several implementations of tor relay running on the network is a
actually a great idea: this improves the security of the network (a bug found
in an implementation might not be present in an other one), and helps to find
bugs or specification issues, which is a **great thing** in my opinion.

For example, [CVE-2018–17144](https://nvd.nist.gov/vuln/detail/CVE-2018-17144)
was [likely found](https://medium.com/@awemany/600-microseconds-b70f87b0b2a6)
due to implementation disparities between different bitcoin clients.

The tor network doesn't put much trust into relays themselves: any entity is
free to run whatever nodes it wants, this is how the network is designed to
work. Although, abuses might happen, and this is why there as several
[documented](https://blog.torproject.org/how-report-bad-relays) countermeasures
and monitoring projects: Volunteers are running continuous checks to measure
the integrity and trustworthiness of exit-nodes: are they tampering with the
traffic or running active analysis? Malicious nodes are flagged and blacklisted
from the network on a continuous basis.


> If the security of the network is ensured by the fact
that all the nodes run the same source code, with the same
security level, the same options and so on. . . this fact proves
that the TOR network is not so secure.

It's absolutely not the case, as explained in the previous paragraph.  It seems
that *Filiol et al.* have no idea about the threat model nor implementation of
the Tor network at all.

> We have discovered that with only few exchanges with the TOR
foundation, we can add a custom node (possibly malicious).
As for every node, no systematic control is possible by the
TOR foundation, once accepted within in the network, we
can do what we want with this node, log the traffic, insert
biases in the creation of circuits etc. . . In summary, we think
that the TOR project should not accept custom codes in
order to respect the uniformity of the network that ensures
“security”.

As previously explained, the only way to add a node to the network is to
register it to the authorities, there is no such thing as "few exchanges with
the TOR foundation", since the network isn't managed by it, nor by anyone,
expect the authorities.

The very fact that anyone can run a relay **ensures** the security and
anonymity of the network: imagine if a single entity would approve or reject
who could join tor…

> As far as confidence is concerned, nobody
> (except state organization) has the courage/time to read the
> source code and no one is paying attention to the designer of
> the changes on the TOR source code

A quick glance at the `git showlog` gives a rough estimate (there might be
duplicates) of the number of committers:

```
$ git log --format='%aN' | sort -u | wc -l
203
$
```

This is a conservative estimation of the people that not only bothered to read
the code, but even contributed to it.

As a comparison this is the same command run on
[GNUPG's git repository](http://git.gnupg.org/cgi-bin/gitweb.cgi?p=gnupg.git),
the library that everyone uses to encrypt emails and sign software
in the Linux world:

```
$ git log --format='%aN' | sort -u | wc -l 
57
$
```

An other indicator of the attention that Tor is getting might be
activity on [Tor's bugtracker timeline](https://trac.torproject.org/projects/tor/timeline),
where it's not uncommon to have more than 100 different actions per day,
by a lot of different people.

> Paul Syverson (from the US NRL) is the original designer (not developer) of
> most of implementation. The last version of TOR is the perfect example: all
> major changes are coming from the US NRL.

We already debunked this by looking at the git commit history.

> No official statement revels that the US government is
> helping the TOR network but all the information gathered
> during our study seems to confirm that the US government
> is still deeply involved in the TOR project

The [sponsors page]( https://www.torproject.org/about/sponsors.html.en ) is
public, and lists every major sponsors. The fact that the US government is
giving grants to researcher to study anonymity and resilience is pretty
healthy for the Tor Project, and doesn't mean, at all, that the US government
is "deeply involved" in the project. At least not significatively
more that the other major donators like the [EFF](https://www.eff.org/), [Human
right Watch](http://www.hrw.org/),
[Google](http://code.google.com/opensource/), the [Freedom of the Press
Foundation](https://freedom.press/), [Reddit](https://www.reddit.com/), …


> This study is not claiming breaking the TOR network
or affirms that the US government is the real organization
behind the TOR project.

This blogpost is not claiming that E. Filiol is a clown,
nor affirms that he hasn't done any worthy contribution to computer science in
years. 

> However favoring such a network
would be a clear violation of the Wassenaar Agreement
(www.wassenaar.org) unless some sort of control is
in place in a way or another (Filiol, 2013).

The paper cited here (Filiol, 2013) is "The Control of Technology by Nation States –
Past, Present and Future – The Case of cryptology and Information
Security”, Journal in Information Warfare, vol. 12, issue 3, pp. 1—10,
October 2013.", published [behind a paywall](https://www.jinfowar.com/journal/volume-12-issue-3/control-technology-nation-state-past-present-and-future-%E2%80%93-case-cryptology). Fortunately, it's possible to access it via
[Google books](https://books.google.fr/books?id=CrIVBAAAQBAJ&pg=PA62&lpg=PA62&dq=%22The+Control+of+Technology+by+Nation+State:+Past,+Present,+and+Future%22&source=bl&ots=Rk6kNn0bnY&sig=oijg5-nluk-Ptfha2lGWNXDQS3g&hl=en&sa=X&ved=2ahUKEwiQ-obaxNbdAhXmtIsKHV_QC2EQ6AEwA3oECAgQAQ#v=onepage&q=%22The%20Control%20of%20Technology%20by%20Nation%20State%3A%20Past%2C%20Present%2C%20and%20Future%22&f=false).
In this paper, Filiol is speaking mostly about France,
while The Tor Project, Inc. is an American entity, but this doesn't matter much
in our case.

Since I'm not a lawyer, I asked a good friend of mine, who happens to be a
legal advisor, specialised in international and French business' Law,
to help me with this part.

The [List of Dual -Use Goods and Technologies and Munitions List]( https://www.wassenaar.org/app/uploads/2018/01/WA-DOC-17-PUB-006-Public-Docs-Vol.II-2017-List-of-DU-Goods-and-Technologies-and-Munitions-List.pdf) states that "*Controls do not apply to "technology" "in the public domain", to "basic scientific research" or to the minimum necessary in formation for patent applications.*".

A quick looks at the *definition* part of the document shows the following:
*"In the public domain": This means "technology" or "software" which has been
made available without restrictions upon its further dissemination.  Note:
Copyright restrictions  do  not  remove  "technology"  or  "software"  from
being "in the public domain".*

This is the case of Tor, and other Free (as in freedom) software, that are thus
not subject to the Wassenaar Agreement, at all.
A quick glance at the
[comprehensive FAQ](https://blog.rapid7.com/2015/06/12/wassenaar-arrangement-frequently-asked-questions/) from rapid7
about the [Wassenaar Arrangement](https://www.wassenaar.org),
or the [small blog post from GNU](https://www.gnu.org/philosophy/wassenaar.en.html)
confirms our interpretation.


> This study aims at informing TOR users and to make them aware
of network like the TOR network and the possible reality
behind. Customers need to be informed before using any
network who claims to protect your privacy and anonymity.

This blogpost aims at informing the public and to make it aware of charlatans
like E. Filiol and the possible reality behind. People need to be informed
before citing any work from this person, inviting him at conferences, or asking
his opinion.

# Conclusion

This is a botched paper in broken English, filled with approximations
and sheer inventions about Tor.
