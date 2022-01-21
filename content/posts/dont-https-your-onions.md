---
title: "Don't HTTPS Your Onions"
date: 2017-12-20
slug: 2017-12-02-dont-https-your-onions
type: posts
draft: false
categories:
  - default
tags:
  - onion-service
---

*This post first appeared on my old blog in December 2017. It is preserved, but
maybe not updated, here.*

---

Unless you're an edge case (which you aren't).

[[!toc levels=2]]

# Why you would want HTTPS

Let's talk about why you normally want HTTPS. Let me know if I missed
something.

## End-to-end encryption

You already get this with Tor.

Everything between your local Tor client (using Tor Browser? It runs Tor in the
background) and the Tor client providing the onion service is encrypted. No Tor
relay and no network-level adversary can tell what onion service you are
visiting (which is actually _better_ than what HTTPS-without-Tor to a regular
website would get you).

If you're an onion service operator and you're at the sophistication level of
taking advice from random blogs on the Internet, HTTPS doesn't help you here.
If you're Facebook, Reddit, or YouTube, then you have a sizable datacenter(s)
and are probably no longer running Tor on the same machines as your webservers.
Unencrypted traffic may be flowing over an uncomfortable distance on your
(super secure, right?) network. Maybe you want HTTPS. __But you also have the
resources to get a valid certificate for your onion. So do *that*__.

## Avoid men in the middle

You already get this with Tor. This is related, but distinct from the previous
point.

When you connect to reddit.com with HTTPS, how do you know no one is MitM'ing
you? The certificate is valid, right? No big scary browser errors. For better
or for worse, we trust the Certificate Authority (CA) system.

When you connect to an onion service, how do you know no one is MitM'ing you?
Easy. It's impossible. The bad guy would have to be in your browser (more
accurately: between the browser part of Tor Browser and the Tor process it runs
in the background) or between the Tor process the onion service operator is
running and the webserver it's pointing at. If you assume your Tor Browser
hasn't been compromised, and you assume the onion service is being run
intelligently, then a MitM attack is impossible. (And if the onion service
isn't being run intelligently, can you really trust its operator to do HTTPS
intelligently?)

## Tie the website to a trusted name

Better solution: encourage the use of bookmarks. 

If you create a web game and self-signed certificate for 5rqvahiexxwm4p6m.onion
and you want your users to know they are connecting to the real web game, tell
them to use a bookmark.  The bad guy can also generate a self-signed
certificate.  The bad guy can also generate a similar onion service name
(making an arbitrary 8 characters match should be rather trivial these days).
No one is checking every character matches what they expect every time. They
just glace at best. And if they glance too fast, the bad guy successfully
spoofed your hostname and your website's bad, self-signed certificate behavior.
Your certificate added nothing of value.

Quick. Which of the following is the real DuckDuckGo onion service?

- https://3q2vglzca6klwz5n.onion/
- https://3g2upl4pq6kufc4m.onion/

(And assume both use self-signed certificates)

Only 5 characters match exactly, and 6 more are in the same "class" (I replaced
the real letter with another short letter [like 'n'] or another letter with a
tail [like 'g']). The remaining 5 are random.

An attacker has a lot of wiggle room. And I do not believe vanity addresses
(such as "coolgamez2f89e4r.onion") help. If it was easy for you to generate an
address that starts with "coolgamez", then it's easy for everyone else. In
fact, if your adversary is significantly more powerful than you, they, might
even try matching some of those random characters at the end. Finally, it may
be lulling your users into a false sense of security. They may be _only_
looking for the "coolgamez" prefix.

So invalid certifcates do nothing to help tie your onion address to a trusted
name.

See also the related discussion elsewhere on the Internet regarding Let's
Encrypt and domains doing Bad Things. Let's Encrypt will happily give you a
certificate for g0ogle.com if you can prove you own the domain. I think that's
fine, I just want to point out the parallels. All a (valid) DV certificate gets
you is proof that you are connecting securely to some domain. It doesn't prove
you're connecting to the domain you intended. You need an EV certificate for
that, and for your users to actually look at the address bar.

# Okay, but ...

So you still want HTTPS for some reason. Okay. Don't get an invalid or
self-signed cert. Seriously.

## No one checks them

There's probably about 10 people out of 7 billion that can honestly claim they
check the certificates they get __every time__ they visit websites. Those 10
people aren't visiting your onion service. So for whom are you adding this
__broken and invalid__ certificate? No one. So __no one will notice__ when it
changes when the impossible MitM happens.

## It teaches bad habits

Invalid certificates produce big scary warnings in browsers. __And they
should__. Something very fishy (phishy) could be going on.  We you add a
self-signed or invalid certificate to your onion service, you are training
users to

1. expect HTTPS when it isn't even necessary
2. click through big dangerous warnings
3. believe brokenHTTPS-over-onion is better than just http-over-onion

That's not okay. Please stop.

## It's just for me

The onion service is just a private thing for you? Great. Do whatever you want,
but don't pretend you're making your service more secure. If you want your
thing to be secure, you run Tor on the same box as the service it is
onion-izing and you secure that box. A self-signed certificate on top of that
is just added work and added headache every time you visit your site.

## I have a valid .com certificate and want to present it for my .onion

See: No one checks certificates. We already covered this.

No one is actually going to check the certificate is the same when they visit
the regular website as when they visit the onion service. You're training your
users to expect a certificate that won't validate for a mismatched hostname,
and they aren't going to notice when the certificate stops being yours and
changes to the bad guy's instead.

## I can actually get a valid certificate for my .onion

Nice! Depending on how important of an onion service you are running, I'm still
tempted to claim you don't _need_ it. If you're datacenter-scale, then I think
you should. If you're just about anything else, it's pointless.

# Final thoughts

Maybe someday Let's Encrypt will offer free valid certificates for onion
services. If that happens, then my opinion half changes. It's still most likely
unnecessary for security reasons. But if you run a game forum and can get both
coolgamez.com and coolgamezxxxxxxx.onion _in the same certificate_, that's
pretty cool. __That__ actually means something.
