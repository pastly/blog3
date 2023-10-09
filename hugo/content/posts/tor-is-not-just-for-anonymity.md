---
title: "Tor Is Not Just for Anonymity"
date: 2022-11-09
slug: 2022-11-09-tor-is-not-just-for-anonymity"
type: post
draft: false
categories:
  - default
tags:
  - tor
  - onion-service
---

## Preamble

Anonymity, privacy, and security. All good things, you'll agree if you're
reading this post. But what we can't all quite agree on is where one stops and
the next begins.

It is my opinion that security is an umbrella term: a more general word that
encompasses both of the others. Everything that makes you more anonymous (or
private) also makes you more secure.

There is a notion that comes up every now and then that Tor doesn't make you
more secure, but it only makes you anonymous. This is obviously not true under
my definitions of the terms (if it makes you anonymous, it *by definition of
the words* must also make you more secure). But here I'll strive to convince
you that even if you disagree with my definitions, there are benefits to Tor
onion services that cannot be construed as anonymity.

## The setup

The framing for this is two scenarios. Either you (1) visit a website on the
regular web using TLS (HTTPS), or (2) visit a regular onion service.
Everything in both scenarios is setup in a typical/sane way. Here are the
assumptions:

- The onion service is a regular 6 hop one. It is not setup to use the
  non-anonymous 3 hop design.
- The user's and server's Tor clients are extremely close to the end point
  software such that for the purpose of discussion here, they *are* the end
point software.
- The regular website uses TLS in a typical way. A reputable Certificate
  Authority (CA) is used, sane ciphers are used, and TLS 1.2 or 1.3 is used.
- DNSSEC is not used. Effectively no one uses it, and if they do, not fully
  correctly.
- DNS over HTTPS is not used. If it is, then it's still vulnerable to attacks
  on TLS and the DNS server changing or censoring results.
- There are no security destroying bugs in TLS libraries or in the relevant
  parts of Tor code.
- Encryption algorithms are not broken. AES is secure, as is whatever the TLS
  client/server negotiate. Crypto is not a weak link.

Tor onion services are not limited to being HTTP servers (they could be IRC,
SMTP, or any other TCP-based daemon), but in this post we ignore everything but
HTTP servers.

## Tor benefits that I'd consider anonymity

- 5/6ths of the path between the user and the server does not know the user. I
  do not just mean the relays, but also the connections between them.

- Similarly, 5/6ths doesn't know the destination. Well actually ...

   - The onion service's guard can tell based on traffic patterns that it is a
     guard for an onion service. Yet while the onion service's guard knows its
IP address, the guard doesn't know *which* onion service it is acting as a
guard for. This means no one knows the destination onion address. Nice! Well
actually ...

   - If the guard *already knows* the onion address (say it's a popular
     publicly known address), it can perform a timing attack to confirm that it
is the guard for the onion service. And now we're back to 5/6ths of the path
doesn't known the destination.

- 100% of the path doesn't know both.

## Tor benefits that are **not** anonymity

- DNS hijacking is impossible. DNS is simply not used.

- The DNS-like process Tor uses is secure (find onion's Introduction Points
  (IP) in the DHT, connect to an IP and to tell onion what Rendezvous Point
(RP) to use, both parties connect to RP). No one knows what onion was looked up
in the DHT: not even the relay in the DHT that held the answer. DNS is
laughably insecure compared to this. The DNS server knows everything (user,
question, and answer). If any part of the link between user and server is
insecure, that's a place everything can be determined by anybody watching. The
DNS server can forge or censor responses whenever it wants. Likewise for anyone
on an unprotected part of the link.

- BGP hijacking is impossible. Every interaction a Tor client has with a relay
  or onion service is authenticated such that you are guaranteed to be
interacting with the relay/onion that you intend to be.

- MITM attacks are impossible. When visiting a regular website, you have to
  assume the none of the 100s of CAs that you trust have maliciously or
mistakenly issued a certificate for the domain you're visiting when they
shouldn't have. There are zero places a corporate firewall can inject itself to
decrypt the traffic. There are zero places and zero parties between the Tor
clients that a MITM attack can be performed. TLS attempts this and usually
succeeds. Tor guarantees it.

If it looks like you've successfully connected to an onion service, you *have*
and you have done so securely. TLS offers no such guarantee.

## Moving on ...

> *Matt, you're just continuing to describe a reimplementation of Transport
> Layer Security.*

No, I'm not. To restate what I've exhaustively said above:

1. TLS isn't used in every part of the process of connecting to a regular
   website. Tor makes the whole process secure.

2. TLS tries its best to ensure your link is secured, but Tor guarantees it.
   With TLS you have to make assumptions you shouldn't have to make in order to
believe it is working. Or put another way: Tor requires fewer assumptions, so
Tor is more secure.

Accessing Tor onion services is designed to be more secure than accessing
something over TLS.

TLS has patches upon patches trying to make it better: Certificate
Transparency, HSTS, OCSP ... These help! Absolutely these make TLS better and
more secure.

But Tor is *more* secure. *Every* onion service is secure and you make fewer
assumptions.

Will the next regular website you visit use HSTS? If you check after you
connect in order to determine the answer, and you find that it isn't using
HSTS, is that because you're being attacked or does the site legitimately not
use HSTS?

Does your browser check CT logs, and if it does, what does it do in response to
failing to find the certificate in CT logs?  Do you assume the CT lookup
process is secure? Are the parties you're communicating with misbehaving? Are
your lookups in CT logs being logged and associated with you?

Tor is not just for anonymity. It provides real, measurable, enumerable
security benefits over TLS.
