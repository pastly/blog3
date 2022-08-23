---
title: "Tor is not 'TOR'"
date: 2021-02-22
slug: 2021-02-22-tor-spelling
type: posts
draft: false
categories:
  - default
tags:
  - tor
---

[paper]: https://www.acsac.org/2011/program/keynotes/syverson.pdf
[paul]: https://www.syverson.org/
[roger-email]: https://lists.torproject.org/pipermail/tor-dev/2002-September/002363.html

Updated: August 2022 to backpedal on Tor not standing for "the onion router."
It can stand for two things depending on whether you ask Paul or Roger.

Warning: pedantry. I'm writing this down once so I have something to refer to
in the future when I want to find [this PDF][paper] again.

[Dr. Paul Syverson][paul] is "the father of onion routing." He and his
colleagues at NRL 20 years ago created onion routing, and he plus Nick
Mathewson and Roger Dingledine wrote the origin tor code (adapted from code
Matej Pfajfar wrote) in the early 2000s.

In short: Dr. Syverson is an authority figure in this space and knows what he's
talking about. He was there and **he is a primary source.**

In 2011 he gave a keynote at ACSAC about the history of onion routing. The PDF
is located [here][paper]. The paragraphs before section 4.1 on page 129 explain
how it's not "TOR" and never was:

> It was also [Roger's] decision that it should be written ‘Tor’ not ‘TOR’.
> Making it more of an ordinary word in this way also emphasizes the overlap of
> meaning with the German word ‘Tor’, which is gate (as in a city gate).

Paul goes on to expain that tor is an acronym that stands for "the onion
routing":

> Thus, when [Roger] told people he was working on onion routing, they would
> ask him which one. He would respond that it was *the* onion routing, the
> original program of projects from NRL. It was Rachel Greenstadt who noted to
> him that this was a nice acronym and gave Tor its name. Roger then observed
> that it also works well as a recursive acronym, ‘Tor’s onion routing’.

However, [here][roger-email] is Roger saying tor stands for "the onion router":

> Too many people have been telling me lately that 'or' is too generic. "I'm
> building onion routing." "Oh, really, which one?" "No, I'm building the
> onion routing design." "Yeah, I know, which one?"
>
> But we really are building *the* onion routing design; not just another
> spin-off design.
>
> And so I dub us tor -- the onion router.

Tor is an acronym that stands for either "the onion router" or "the onion
routing." It is not -- and never was -- spelled "TOR."
