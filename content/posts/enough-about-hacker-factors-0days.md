---
title: "Enough about Hacker Factor's '0days'"
date: 2021-02-22
slug: 2021-02-22-enough-about-hacker-factors-0days
type: posts
draft: false
categories:
  - default
tags:
  - tor
  - rebuttal
  - rant
---

*This post first appeared on my old blog in February 2021. It is preserved,
but maybe not updated, here.*

---

[TP rebuttal]: https://twitter.com/torproject/status/1288955073322602496

Last summer Dr. Neal Krawetz AKA "Hacker Factor" made a series of posts on his
blog about Tor "0days." This post is a summary of [Tor Project's response][TP rebuttal]
to **one** of his posts. Neither this post nor Tor Project's tweet serve as a
perfect point-by-point rebuttal of everything he claims in the post, nor all of
his "0day" posts. The things that he says that are skipped over here are not
automatically valid just because they are skipped. The *theme* of the responses
hold for just about everything he ever says about Tor. As they say, *it's
easier to spread bullshit than it is to refute it*.

Okay wait. Many of the things he says aren't bullshit. He has some valid
points. He just can't express those points in a productive manner anymore.
His Tor posts are riddled with phrases that instantly put Tor people on the
defensive, so it's a masochistic exercise to review them again every time
someone asks "hey, what's your thoughts on this HF guy's post from last year?"

The [Tor Project tweet][TP rebuttal] is a level headed response (that I helped write); again, this is
just a summary of that response, and I'm taking the opportunity to vent while
writing it. I will take no questions or comments, nor read emails about this
post. I'm freely using inflammatory, emotionally charged language because--
unlike HF--I do not expect, or want, a conversation to come out of this.
This is a crass cathartic exercise for me.

The title of the HF blog post this post deals with is "Tor 0day: Burning
Bridges." You can find it with your favorite search engine; I'm not going to
help drive traffic to his site.

Here we go. The actual content of this "short" post I'm writing for my own
reference. Links to additional anti-HF texts on the Internet are at the end of this post.

# Use of the word 0day

HF knows exactly what he's doing when he uses the term "0day." He's not stupid.
He knows what people immediately think when they here that term. He knows 0day
sounds scary and gets people excited about a dangerous new discovery.
He knows he'd get media attention.

He hides behind "well technically I'm correct because one of the little-used
definitions of 0day includes things that aren't fixed and exist in the wild."
You're technically and pointlessly correct, HF. And every time someone calls
you out on this inflammatory word choice, you get the free rebuttal of "you're
not even addressing the real issues! You just don't like my (perfectly
valid!!!1!) word choice. You clearly have nothing." No. Fuck you. Use this
excuse again if/when you see this, then fuck right off.

# Scrollbar width

[22137]: https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/22137

This is (and was) a [publicly documented information leak][22137]. There are
many ways the user's OS can be leaked (one of them is even on purpose!), and
fixing just one of them without fixing many of the others is pointless.

People should report bugs like this so they can be documented and fixed in
batches. People should *not* throw a hissy fit when the bug isn't fixed right
away in order to validate their sense of self-importance.

# Tor's TLS fingerprint

[since 2007]: https://gitweb.torproject.org/torspec.git/tree/proposals/106-less-tls-constraint.txt
[anti-yasha]: https://blog.erratasec.com/2018/03/askrob-does-tor-let-government-peek-at.html
[anti-yasha archive]: https://web.archive.org/web/20180320084222if_/https://blog.erratasec.com/2018/03/askrob-does-tor-let-government-peek-at.html

The way Tor uses TLS between relays and between a client and their relay is
(and always has been) fingerprintable. This has been publicly known [since
2007][]. Before HF, it was brought up in 2018 in a much more slanderous and
make-a-name-for-yourself-at-the-cost-of-others [tone][anti-yasha] ([archive copy][anti-yasha archive]).

HF's proposed solution is the wrong one. Tor Project has decided on a better
one: bridges with pluggable transports.

# Obfs4 is identifiable

Perhaps surprisingly, this is known. It's also an important problem. It's being
worked on at a pace slower than HF finds acceptable.

But HF presents variations on known attacks without evidence that they work at a
large scale. Two possible issues: too much state to keep track of, or too many
false positives such that the adversary is unwilling to deploy it. Luckily for
HF, the bar for publishing "science" in a blog post is on the ground. He can
say things confidentially and non-experts believe him. Shame on you, HF.

He further shows that he barely looked into this before putting pen to paper
(or fingers to keyboard?) by

- admitting to not knowing of any prior work (in response Tor Project points
  him to some),

- citing a paper to support the claim that the Great Firewall can detect obfs4
  when the paper say the opposite,

- citing a blog post about obfs4 bridges being blocked in China, then ignoring
  that the issue discussed therein is about bridge distribution. Remember HF,
in this section you were talking about fingerprintable network activity.


# Additional links

- [Top comment on HN posting of his "Tor 0day: Finding IP Addresses"](https://news.ycombinator.com/item?id=24504422)
- [Most top-level comments on the HN posting of his "Tor 0day: Stopping Tor Connections"](https://news.ycombinator.com/item?id=23929312)
- [Links from a HN comment to his "OMG I'm being port scanned!! I'm being attacked!!" posts](https://news.ycombinator.com/item?id=18523549)
